# Plant-Timelapse
Records a timelapse of plants.

An IP camera (Wansview 2K G6) is monted on a adjustable arm and stream a top view of the plants on the cloud and locally via RTSP. A SBC (single board computer) (Raspberry Pi 3B) executes a cron job every day at noon to save a timelapse of the plant. Additionally, the cloud stream support real-time view of the camera and control of the LED lights.

The SBC is kept indoors, protected from environmental damage and burglary. The arm sub-system is low cost and custom made, reducing the risk of burglary and cost of replacement.

The camera module is configured to stream locally with a RTSP protocol, which is compatible to OpenCV `VideoCapture` class. 

<img src="images/planter.jpeg" width="500"/>

Figure 1. Arm-subsystem mounted on the planter

<img src="images/timelapse.png" width="500"/>

Figure 2. Sample of the top view capture

<img src="images/app.jpeg" width="300"/>

Figure 3. Screenshot of the app streaming real-time view of the planter


### Components:
- Camera module (Wansview 2K G6)
- Raised bed planter (Self-Watering Elevated Cedar planter - 23" x 49" x 30"H)
- Custom camera arm support
- Raspberry Pi 3B

## Adding Cron Job

**E**dit cron job list with `$ crontab -e` and append:

`0 * * * * python3 /home/garamizo/Software/Plant-Timelapse/cam_snapshot.py` 

to execute `cam_snapshot.py` every hour (assuming this package is located at `/home/garamizo/Software`).

## Mechanical Design

| <img src="images/explode_arm.png" height="400"/> | <img src="images/explode_head.png" height="400"/> |
| --- | --- |
| Figure 4a. Arm assembly | Figure 4b. Head assembly |

## Camera Breakdown

IP camera model *Wansview 2K G6* features 
- 3 MP (2304 x 1296 px)
- Vertical Angle of view: 50 deg
- Horizontal Angle of view: 80 deg
- LED lights
- Infrared LED
- Infrared camera filter
- *Microphone*
- *Speaker*
- *Motorized pan and tilt (2x 24BYJ48 stepper motors)*
- *Wansview App to control lights and streaming*

<img src="images/lamp.jpeg" width="500"/>

<img src="images/sensor2.jpeg" width="500"/>

<img src="images/sensor.jpeg" width="500"/>

<img src="images/power.jpeg" width="500"/>
