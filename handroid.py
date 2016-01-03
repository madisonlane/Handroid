#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO, time

# ===========================================================================
# Example Code
# ===========================================================================
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(17, RPi.GPIO.IN,pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(18, RPi.GPIO.IN,pull_up_down=RPi.GPIO.PUD_UP)

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

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

#initalize fingers to High Five position
pwm.setPWM(5, 0, 290)
pwm.setPWM(4, 0, 524) 
time.sleep(.50)
pwm.setPWM(3, 0, 524)
time.sleep(.50)
pwm.setPWM(2, 0, 209)

while (True):
    if RPi.GPIO.input(17) == RPi.GPIO.LOW:
      print("Fist Bump pressed.")
      pwm.setPWM(3, 0, 325)
      time.sleep(.50)
      pwm.setPWM(2, 0, 535)
      time.sleep(.50)
      pwm.setPWM(5, 0, 599)
      pwm.setPWM(4, 0, 151)
      
    if RPi.GPIO.input(18) == RPi.GPIO.LOW:
      print("High Five pressed.")
      pwm.setPWM(5, 0, 290)
      pwm.setPWM(4, 0, 524)
      time.sleep(.50)
      pwm.setPWM(3, 0, 524)
      time.sleep(.50)
      pwm.setPWM(2, 0, 209)

RPi.GPIO.cleanup()


