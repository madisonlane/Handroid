# Handroid
Python programs for controlling a homemade robotic hand on Raspberry Pi using the Adafruit ServoHat PWM module to drive 5 servo motors.  
Servo's 1&2 control wrist servos, 3 & 4 control thumb servos, 5 controls index finger servo, and servo 6 controls middle/ring/pinky finger servo (all three finger's tendons are connected to the same servo).  There two SPST micro switches control open/closing hand positions.  The switches are wired via GPIO pin 17 & 18.

# Getting Started
Clone this repository.
```
git clone https://github.com/madisonlane/Handroid.git
```

Run handroid.py
```
sudo python handroid.py
```

# Files

*handroid.py* - Program that reads GPIO pins and opens or closes the hand.  Hand initial position is open.

*handroid-with-wii.py* - Program that uses wii remote to control individual servo positions.  Used to obtain the servo position values in the handroid.py program.

*handroid-servo-tester.py* - Program that cycles all servos between min and max positions.  Used to test that servos and servo hat is working properly.  This is a modified version of the servohat PWM test program that comes from Adafruit's python libraries found on github.
