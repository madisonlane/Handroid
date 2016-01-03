#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO, time
import cwiid

# Initialize GPIO pins 17 & 18 with pull up resistor (for button input)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(17, RPi.GPIO.IN,pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(18, RPi.GPIO.IN,pull_up_down=RPi.GPIO.PUD_UP)

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
buttonDelay = 0.1 # Delay in milliseconds to wait after a button has been pressed
wiiRemote = False # Boolean value which will be set true if WiiRemote is detected. 

# Connect to the Wii Remote...if it times out, continue on and just use buttons on breadboard.
print 'Press red reset button near batteries on Wii remote, then'
print 'Press the 1 & 2 buttons at the same time.'
print 'If you do not want to use Wii Remote, wait a few seconds to continue.'

try:
  wii = cwiid.Wiimote()
  wiiRemote = True
except RuntimeError:
  wiiRemote = False
  print "Could not find a Wii Remote, continuing on."

if wiiRemote:
  wii.rpt_mode = cwiid.RPT_BTN
  print "WiiRemote connected."
  print 'Select servo: A=Wrist, B=Thumb, 1=Index Finger, 2=Fingers'
  print 'Arrows: increase/decrease position of selected servo'
  print 'Home: Reset all servo positions.'

print "Press Fist Bump or High Five buttons, or buttons on Wii Remote."

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Set initial position of all joint servos to be 1/2 way between min and max values
wrist_joint0_position=servoMin+(servoMax-servoMin)/2 
wrist_joint1_position=servoMin+(servoMax-servoMin)/2 
thumb_joint0_position=servoMin+(servoMax-servoMin)/2 
thumb_joint1_position=servoMin+(servoMax-servoMin)/2 
finger0_position=servoMin+(servoMax-servoMin)/2 
finger1_position=servoMin+(servoMax-servoMin)/2 

WRIST=0
THUMB=1
INDEX=2
FINGERS=3
controlling=WRIST
print 'Currently controlling wrist.'

while (True):
    # Get the current state of buttons on the Wii Remote
    if wiiRemote:
      buttons = wii.state['buttons']
      # A and B buttons switch control between thumb and wrist
      if (buttons & cwiid.BTN_A) and not (controlling == WRIST):
        print 'Controlling Wrist'
        controlling = WRIST
      if (buttons & cwiid.BTN_B) and not (controlling == THUMB):
        print 'Controlling Thumb'
        controlling = THUMB
      # 1 and 2 buttons switch control between fingers
      if (buttons & cwiid.BTN_1) and not (controlling == INDEX):
        print 'Controlling Index Finger'
        controlling = INDEX
      if (buttons & cwiid.BTN_2) and not (controlling == FINGERS):
        print 'Controlling Fingers'
        controlling = FINGERS
      if (buttons & cwiid.BTN_HOME):
        print 'Resetting to home positions'
        wrist_joint0_position=servoMin+(servoMax-servoMin)/2 
        wrist_joint1_position=servoMin+(servoMax-servoMin)/2 
        thumb_joint0_position=servoMin+(servoMax-servoMin)/2 
        thumb_joint1_position=servoMin+(servoMax-servoMin)/2 
        finger0_position=servoMin+(servoMax-servoMin)/2 
        finger1_position=servoMin+(servoMax-servoMin)/2 
        pwm.setPWM(0, 0, wrist_joint0_position)
        pwm.setPWM(1, 0, wrist_joint1_position)
        pwm.setPWM(2, 0, thumb_joint0_position)
        pwm.setPWM(3, 0, thumb_joint1_position)
        pwm.setPWM(4, 0, finger0_position)
        pwm.setPWM(5, 0, finger1_position)

      # WRIST CONTROL
      if controlling == WRIST:
        if (wrist_joint0_position > servoMin) and (buttons & cwiid.BTN_LEFT):
          print 'LEFT pressed, Wrist joint 0 position(servo 0)=' + str(wrist_joint0_position)
          wrist_joint0_position = wrist_joint0_position - 1
          pwm.setPWM(0, 0, wrist_joint0_position)
 
        if (wrist_joint0_position < servoMax) and (buttons & cwiid.BTN_RIGHT):
          print 'RIGHT pressed, Wrist joint 0 position(servo 0)=' + str(wrist_joint0_position)
          wrist_joint0_position = wrist_joint0_position + 1
          pwm.setPWM(0, 0, wrist_joint0_position)

        if (wrist_joint1_position > servoMin) and (buttons & cwiid.BTN_UP):
          print 'UP pressed, Wrist joint 1 position(servo 1)=' + str(wrist_joint1_position)
          wrist_joint1_position = wrist_joint1_position - 1
          pwm.setPWM(1, 0, wrist_joint1_position)
 
        if (wrist_joint1_position < servoMax) and (buttons & cwiid.BTN_DOWN):
          print 'DOWN pressed, Wrist joint 1 position(servo 1)=' + str(wrist_joint1_position)
          wrist_joint1_position = wrist_joint1_position + 1
          pwm.setPWM(1, 0, wrist_joint1_position)
      if controlling == THUMB: 
        # THUMB CONTROL
        if (thumb_joint0_position > servoMin) and (buttons & cwiid.BTN_LEFT):
          print 'LEFT pressed, thumb joint 0 position(servo 2)=' + str(thumb_joint0_position)
          thumb_joint0_position = thumb_joint0_position - 1
          pwm.setPWM(2, 0, thumb_joint0_position)
 
        if (thumb_joint0_position < servoMax) and (buttons & cwiid.BTN_RIGHT):
          print 'RIGHT pressed, thumb joint 0 position(servo 2)=' + str(thumb_joint0_position)
          thumb_joint0_position = thumb_joint0_position + 1
          pwm.setPWM(2, 0, thumb_joint0_position)

        if (thumb_joint1_position > servoMin) and (buttons & cwiid.BTN_UP):
          print 'UP pressed, thumb joint 1 position(servo 3)=' + str(thumb_joint1_position)
          thumb_joint1_position = thumb_joint1_position - 1
          pwm.setPWM(3, 0, thumb_joint1_position)
 
        if (thumb_joint1_position < servoMax) and (buttons & cwiid.BTN_DOWN):
          print 'DOWN pressed, thumb joint 1 position(servo 3)=' + str(thumb_joint1_position)
          thumb_joint1_position = thumb_joint1_position + 1
          pwm.setPWM(3, 0, thumb_joint1_position)

      if controlling == INDEX:
        # INDEX FINGER
        if (finger0_position > servoMin) and (buttons & cwiid.BTN_UP):
          print 'UP pressed, index finger position(servo 4)=' + str(finger0_position)
          finger0_position = finger0_position - 1
          pwm.setPWM(4, 0, finger0_position)
 
        if (finger0_position < servoMax) and (buttons & cwiid.BTN_DOWN):
          print 'DOWN pressed, index finger position(servo 4)=' + str(finger0_position)
          finger0_position = finger0_position + 1
          pwm.setPWM(4, 0, finger0_position)
      if controlling == FINGERS:
        if (finger1_position > servoMin) and (buttons & cwiid.BTN_UP):
          print 'UP pressed, fingers position(servo 5)=' + str(finger1_position)
          finger1_position = finger1_position - 1
          pwm.setPWM(5, 0, finger1_position)
 
        if (finger1_position < servoMax) and (buttons & cwiid.BTN_DOWN):
          print 'DOWN pressed, fingers position(servo 5)=' + str(finger1_position)
          finger1_position = finger1_position + 1
          pwm.setPWM(5, 0, finger1_position)
 

    if RPi.GPIO.input(17) == RPi.GPIO.LOW:
      print("Fist Bump pressed.")
      time.sleep(.25)
      
      for channel in range(5):
        pwm.setPWM(channel, 0, servoMin)
      time.sleep(1)
      for channel in range(5):
        pwm.setPWM(channel, 0, servoMax)
      
    if RPi.GPIO.input(18) == RPi.GPIO.LOW:
      print("High Five pressed.")
      time.sleep(.25)
      for channel in range(5):
        pwm.setPWM(channel, 0, servoMax)
      time.sleep(1)
      for channel in range(5):
        pwm.setPWM(channel, 0, servoMin)
        
RPi.GPIO.cleanup()


