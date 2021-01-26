# Door-locker-using-face-recognition

## Software used

1. OpenCV
2. Thonny IDE

## Hardware used

1. Raspberry Pi 3B+ Board (with all required accessories)
2. Raspberry Pi 5MP Camera module
3. Solenoid lock
4. Relay module
5. Four 9V Batteries (2 strings and 2 in series in each string)

## Steps

1. First we need to open and run the facerecog.py file, it will then ask our name, after we enter the name the Pi camera will get enabled and it will capture photos of our face. The photos are then stored in a folder. These photos are considered the photos of the authorized person. (In this step it is in face train mode).
2. After this we need to open and run the facewithname.py file, again the Pi camera gets enabled and the Solenoid locks opens only when the authorized person's face is detected by the camera.

## Working

- This project basically works on Computer Vision, Image Processing, & ML algorithms.
- The relay module input pin is connected to the GPIO #7 pin and the battery + solenoid lock is connected to the output pin of the relay module.
- The GPIO #7 pin is initialized to active high mode and the solenoid lock is in closed mode.
- When the Pi camera detects the authorized person's face with confidence level above 70%, an active low signal is sent to the realy via the GPIO #7 pin which activates the relay, the battery then gets connected to the solenoid lock and it opens.
- When the Pi camera detects an unauthorized person or an authorized person with less than 70% confidence level, the GPIO #7 pin remains at active high mode and the solenoid remains closed.

**NOTE :** 

-Since the relay module we our using in this device has an inbuilt opto-coupler, the active high is basically low & active low is basically high (reversed).
-Multiple persons can be made authorized in this device.

## Application

Can be used in smart homes or smart cars where the doors get unlocked using face recognition.
