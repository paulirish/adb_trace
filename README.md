# adb_trace: Android Debug Bridge + Chrome Tracing

----------
----------

### This repo's source is no longer updated. 

The documentation below is updated and revised, however the source in this repo is stale.

You will get best results with the `profile_chrome.py` script in the Chromium project.
[Get Chromium source](https://www.chromium.org/developers/how-tos/get-the-code) (with no history, for speed). 
Script is located at `src/tools/profile_chrome.py`
```
cd src/tools
./profile_chrome.py --continuous -z --view
```

If you attempt to use this repo, follow the install instructions at the bottom.

----------
----------


## Grabbing a capture from a stable Chrome and viewing it ##

```sh
./profile_chrome.py --continuous --view

  Capturing chrome trace. Press Enter to stop early...done
  Downloading...done
  Trace written to chrome-profile-results-2013-10-25-181905.html
```

### Common cases
The documentation of all options is available below.

```sh
# Basic capture from stable
#   options: records until buffer full, opens viewer
./profile_chrome.py --continuous --view

# Using dev channel chrome
./profile_chrome.py --browser dev --continuous --view

# Android Systrace provides more detailed low-level statistics
  # List systrace categories available to record
./profile_chrome.py --systrace list

  # Record a systrace
./profile_chrome.py --systrace gfx,input,view,sched,freq    --continuous --view

```

By default we also record a normal Chrome trace in addition to the [Android Systrace](http://developer.android.com/tools/help/systrace.html). This can be controlled with the --categories flag.

## Viewing a capture ##

If you leave off `--view` flag (to open it immediately), you can open the created .json file (`chrome-profile-results-YYYY-MM-DD-hhmmss.json`) in `chrome://tracing`.

## Command Line Options ##

```sh
./profile_chrome.py --help
```
Usage: profile_chrome.py [options]

Record about://tracing profiles from Android browsers. See http://dev.chromium.org/developers/how-tos/trace-event-profiling-tool for detailed instructions for profiling.

#### General options

     -h, --help            show this help message and exit
     -b BROWSER, --browser=BROWSER
                           Select among installed browsers. One of
                           android_webview_shell, beta, build, chrome,
                           chrome_beta, chrome_canary, chrome_dev,
                           chrome_document, chrome_shell, chrome_stable,
                           chrome_work, chromecast_shell,
                           chromedriver_webview_shell, chromium,
                           components_browsertests, content_shell, dev, stable,
                           "stable" is used by default.
     -v, --verbose         Verbose logging.
     -z, --compress        Compress the resulting trace with gzip.
     -d DEVICE, --device=DEVICE
                           The Android device ID to use.If not specified, only 0
                           or 1 connected devices are supported.

####  Timed tracing:

    -t N, --time=N      Profile for N seconds and download the resulting
                        trace.

####  Continuous tracing:

    --continuous        Profile continuously until stopped.
    --ring-buffer       Use the trace buffer as a ring buffer and save its
                        contents when stopping instead of appending events
                        into one long trace.

####  Chrome tracing options:

    -c CHROME_CATEGORIES, --categories=CHROME_CATEGORIES
                        Select Chrome tracing categories with comma-delimited
                        wildcards, e.g., "*", "cat1*,-cat1a". Omit this option
                        to trace Chrome's default categories. Chrome tracing
                        can be disabled with "--categories=''". Use "list" to
                        see the available categories.
    --trace-cc          Deprecated, use --trace-frame-viewer.
    --trace-frame-viewer
                        Enable enough trace categories for compositor frame
                        viewing.
    --trace-ubercompositor
                        Enable enough trace categories for ubercompositor
                        frame data.
    --trace-gpu         Enable extra trace categories for GPU data.
    --trace-flow        Enable extra trace categories for IPC message flows.
    --trace-memory      Enable extra trace categories for memory profile.
                        (tcmalloc required)
    --trace-scheduler   Enable extra trace categories for scheduler state

####  Systrace tracing options:

    -s SYS_CATEGORIES, --systrace=SYS_CATEGORIES
                        Capture a systrace with the chosen comma-delimited
                        systrace categories. You can also capture a combined
                        Chrome + systrace by enabling both types of
                        categories. Use "list" to see the available
                        categories. Systrace is disabled by default.

####  Perf profiling options:

    -p, --perf          Capture a perf profile with the chosen comma-delimited
                        event categories. Samples CPU cycles by default. Use
                        "list" to see the available sample types.

####  Java tracing:

    --ddms              Trace Java execution using DDMS sampling.

####  Output options:

    -o OUTPUT, --output=OUTPUT
                        Save trace output to file.
    --json              Save trace as raw JSON instead of HTML.
    --view              Open resulting trace file in a browser.


## trace-event-viewer ##

`trace-event-viewer` is a standalone version of Chrome's about:tracing UI
for viewing multithreaded performance traces. Works on OSX and Linux and
even Windows using Chrome Apps v2 to make it look like a regular app.

It's included as a submodule in this repo: https://github.com/natduca/trace_event_viewer


## Installation ##

1. For this repo (only) Pull in the necessary dependencies with `git submodule update --init`.
1. Install Android SDK. Verify `adb` is in your path
    * http://developer.android.com/sdk/index.html
1. Ensure that your Android device is connected and USB debugging is enabled
    * http://developer.android.com/tools/device.html

