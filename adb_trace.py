#!/usr/bin/python
import subprocess
import re
import os
import sys
import optparse
import time

def call_checked(*args):
  r = subprocess.call(args)
  assert r == 0

def run(*args):
  p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (stdout, stderr) = p.communicate()
  assert p.returncode == 0
  return stdout

def run_and_readlines(*args):
  raw = run(*args)
  lines =  [l.strip() for l in raw.split("\n") if len(l)]
  return lines

def run_and_readlines_strip_empty(*args):
  lines = run_and_readlines(*args)
  return [l for l in lines if len(l)]

def get_display_refresh_rate():
  lines = run_and_readlines("adb", "shell", "dumpsys SurfaceFlinger --latency")
  print lines[:2]
  if len(lines) < 2:
    print "Odd, I didn't get enough commands back from surfaceflinger to gusss refresh rate."
    return 60
  if re.match('^\d+$', lines[1]):
    return 1e9 / float(lines[1])
  if re.match('^\d+$', lines[2]):
    return 1e9 / float(lines[2])

  print "Odd, I didn't get anything snae back from surfaceflinger to gusss refresh rate."
  print "I got [%s, %s]" % (lines[1], lines[2])
  return 60


def get_files():
  files = run("adb", "shell", "ls /sdcard/Download/chrome-profile-results*")
  if re.search("No such file or directory", files):
    return None
  return [f.strip() for f in files.split("\n") if len(f)]

def purge_files():
  run("adb", "shell", "rm /sdcard/Download/chrome-profile-results*")

def pull_result(dst_file):
  time.sleep(5)
  files = get_files()
  if not files:
    raise Exception("No traces on device.")
  files.sort()
  cur_file = files[-1]
  print "Pulling %s to %s" % (os.path.basename(cur_file),
                              dst_file)
  run("adb", "pull", cur_file, dst_file)

def main():
  parser = optparse.OptionParser(usage="adb_trace")
  parser.add_option('--refresh-rate', '-r', dest='refresh_rate', action='store', default=0, help='The refresh rate for the screen, in hertz. If not given, the script will try to autoguess it.')
  parser.add_option('--url', dest='url', action='store', default=None, help='A URL to navigate to before running the test.')
  parser.add_option('-v', '--view', dest='run_tev', action='store_true', default=False, help='Run trace-event-viewer upon completion.')
  parser.add_option('-b', '--browser', dest='browser', action='store', default=None, help='Which browser you want to run against: stable / beta')
  options, args = parser.parse_args()

  start_cmd = "com.google.android.apps.chrome.GPU_PROFILER_START"
  stop_cmd = "com.google.android.apps.chrome.GPU_PROFILER_STOP"

  if options.browser and options.browser == "beta":
    start_cmd = "com.chrome.beta.GPU_PROFILER_START"
    stop_cmd = "com.chrome.beta.GPU_PROFILER_STOP"

  if options.url:
    lines = run_and_readlines_strip_empty("adb", "shell", """am start -d "%s" -n com.android.chrome/.Main""" % options.url)
    print "Press enter when loaded..."
    sys.stdin.readline()

  if options.refresh_rate == 0:
    options.refresh_rate = get_display_refresh_rate()
    print "Refresh rate auto-guessed to be %f." % options.refresh_rate

  purge_files()

  run("adb", "shell", "am", "broadcast",
      "-a", start_cmd)
  can_pull = True
  try:
    print "Press enter to stop profiling."
    sys.stdin.readline()
  except KeyboardInterrupt:
    can_pull = False
  finally:
    run("adb", "shell", "am", "broadcast",
        "-a", stop_cmd)

  if can_pull:
    pull_result('./chrome.json')
    purge_files()

  if can_pull and options.run_tev:
    tev_cmd = ["trace-event-viewer"]
    #if options.refresh_rate != 0:
    #  tev_cmd.append("--refresh-rate")
    #  tev_cmd.append(str(options.refresh_rate))
    tev_cmd.append("chrome.json")
    subprocess.call(tev_cmd)
  return 0

if __name__ == "__main__":
  sys.exit(main())
