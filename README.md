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

# Materials

- Vilros Raspberry Pi2 Kit (includes breakout board, ribbon cable, T-breakout, 2 switches, jumper wires, 330 ohm resistors, power cables) 
  - Logitech Wireless keyboard
  - USB Wifi
  - USB Bluetooth
- Adafruit 16-channel ServoHat PWM module mini kit
- 2 x Mini Pan-Tilt Kit, assembled with servos
- 5V 4A switching power supply
- 2 x Micro servos
- 1 pack of 2 brass M2.5 standoffs for Pi HATs
- 1 GPIO stacking header for Pi 2

- Hot glue gun & glue
- Bag of 1/2" straws
- Dental tape
- 1 box Sculpy polymer clay
- 1/2" x 4" x 8' pine lumber
- 12" x 12" x 3" wood box (for base)
- 2 x small wood screws

