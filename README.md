# A9 P2PIP Camera reader #

## Credit ##
Inspired by https://github.com/K-Francis-H/little-stars-hack/blob/main/camera_feed_pygame.py
A still ongoing thread to this kind of cameras can be found at https://community.home-assistant.io/t/popular-a9-mini-wi-fi-camera-the-ha-challenge

## What it does ##
Trigger the A9 mini WiFi Camera to output it's MJPEG stream.

## Limitations ##
The MJPEG stream does not have sound even though the A9 camera supports sound. There is currently no way to switch the IR LEDs (and possibly an IR mode of the camera). There is currently no way to set SSID and password to use the A9 camera in any other mode than Accesspoint (AP) mode.
There are also other Versions out there. It clould be that your variant of the A9 mini WiFi Camera is not compatible with this script.

## How to use it ##
If you just want to watch the incoming stream you can feed the raw MJPEG stream into the camera like so
```bash
  ./a9.py | ffplay -
```

## Notice ##
I wouldn't be surprised if there were an option to use `ffplay` or other standard software to directly connect to the camera output.

## Changelog ##
*H0ffmann*: Removed the first UDP package to port 8070 as it's not required. Changed script to directly output raw MJPEG data an let `ffmplay` do the cutting and slicing. Stream could also be converted to a format better suitable for streaming. Basicly the only thing the script does is feed the camera with an UDP packages containing the magic byte sequence to initiate MJPEG streaming and then piping this stream from port `8080` to to `stdout`.
