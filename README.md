# adb_trace
# Android Debug Bridge + Chrome Tracing

Requires Android Chrome version 25+

## Prerequisites ##

1. Ensure that the Android SDK is installed and that `adb` is in your path
    * http://developer.android.com/sdk/index.html
1. Ensure that your Android device is connected and USB debugging is enabled
    * http://developer.android.com/tools/device.html
1. Ensure that USB debugging is enabled in Chrome
    * https://developers.google.com/chrome-developer-tools/docs/remote-debugging

## Grabbing a capture from a stable Chrome build ##

```sh
$ python ./adb_trace.py
['SurfaceView', '16954612']
Refresh rate auto-guessed to be 58.981002.
Press enter to stop profiling.

Pulling chrome-profile-results-2013-03-19-014011 to ./chrome.json
```

Using beta?

```sh
$ python ./adb_trace.py --browser beta
```

Using dev channel or developer build? (Sorry, internal only right now)
`--browser dev` and `--browser build`


## Viewing a capture ##

On the computer your Android is connected to:

1. Navigate to `about:tracing`
1. Click the *Load* button
1. Select `chrome.json` that was copied to your PC.

## Command Line Options ##

* `--refresh-rate`: The display refresh rate in Hz.
* `--url`: The url to navigate to before capturing the trace. 
* `--browser`: The browser channel: stable, beta, dev, or build.
    * `stable`: The official build of Chrome
    * `beta`: The beta build of Chrome
    * `dev`: The development/canary build of Chrome
    * `build`: Compiled Chrome yourself? This one is for you.
* `--view`: Runs the `trace-event-viewer` command upon completion.

## trace-event-viewer ##

`trace-event-viewer` is a standalone version of Chrome's about:tracing UI
for viewing multithreaded performance traces. Works on OSX and Linux and
even Windows using Chrome Apps v2 to make it look like a regular app.

You can grab it from here: https://github.com/natduca/trace_event_viewer

