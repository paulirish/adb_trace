# adb_trace
# Android Debug Bridge + Chrome Tracing

Requires Android Chrome version 25+

## Prerequisites ##

1. Ensure that the Android SDK is installed and that `adb` is in your path
    * http://developer.android.com/sdk/index.html
1. Ensure that your Android device is connected and USB debugging is enabled
    * http://developer.android.com/tools/device.html
1. Ensure that USB debugging is enabled in Chrome (enabled automatically for 28+)
    * https://developers.google.com/chrome-developer-tools/docs/remote-debugging

## Grabbing a capture from a stable Chrome build ##

```sh
$ python ./adb_profile_chrome.py --time 5
Capturing 5-second chrome trace. Press Ctrl-C to stop early...done
Downloading...done
Trace written to chrome-profile-results-2013-10-25-181905
```

Using beta?

```sh
$ python ./adb_profile_chrome.py --time 5 --browser beta
```

Using dev channel or developer build? `--browser dev` and `--browser build`

See below for complete list of supported browsers.

## Grabbing a Systrace ##

An [Android Systrace](http://developer.android.com/tools/help/systrace.html)
provides more detailed low-level statistics from the operating system. This is
how to capture one:

$ python ./adb_profile_chrome.py --time 5 --systrace gfx,input,view,sched,freq

By default we also record a normal Chrome trace in addition to the Systrace.
This can be controlled with the --categories flag.

## Viewing a capture ##

On the computer your Android is connected to:

1. Navigate to `about:tracing`
1. Click the *Load* button
1. Select `chrome-profile-results-YYYY-MM-DD-hhmmss.json` that was copied to your PC.

## Command Line Options ##

*  `-h, --help`:        show this help message and exit
*  `-o OUTPUT, --output=OUTPUT`:
                        Save profile output to file.
*  `-b BROWSER, --browser=BROWSER`:
                        Select among installed browsers. One of
                        `android_webview_shell`, `beta`, `build`, `chrome`,
                        `chrome_beta`, `chrome_dev`, `chrome_stable`,
                        `chromium_test_shell`, `content_shell`, `dev`, `stable`,
                        "`stable`" is used by default.
*  `-v, --verbose`:     Verbose logging.
*  `-z, --compress`:    Compress the resulting trace with gzip.
*  `--view`:            Run trace-event-viewer upon completion.

### Timed tracing ###

*    `-t N, --time=N`:  Profile for N seconds and download the resulting
                        trace.

### Continuous tracing ###

*    `--continuous`:    Profile continuously until stopped.
*    `--ring-buffer`:   Use the trace buffer as a ring buffer and save its
                        contents when stopping instead of appending events
                        into one long trace.

### Trace categories ###

*    `-c CHROME_CATEGORIES, --categories=CHROME_CATEGORIES`:
                        Select Chrome tracing categories with comma-delimited
                        wildcards, e.g., "*", "cat1*,-cat1a". Omit this option
                        to trace Chrome's default categories. Chrome tracing
                        can be disabled with "--categories=''".
*    `-s SYS_CATEGORIES, --systrace=SYS_CATEGORIES`:
                        Capture a systrace with the chosen comma-delimited
                        systrace categories. You can also capture a combined
                        Chrome + systrace by enabling both types of
                        categories. Use "list" to see the available
                        categories. Systrace is disabled by default.
*    `--trace-cc`:      Enable extra trace categories for compositor frame
                        viewer data.
*    `--trace-gpu`:     Enable extra trace categories for GPU data.


## trace-event-viewer ##

`trace-event-viewer` is a standalone version of Chrome's about:tracing UI
for viewing multithreaded performance traces. Works on OSX and Linux and
even Windows using Chrome Apps v2 to make it look like a regular app.

You can grab it from here: https://github.com/natduca/trace_event_viewer

