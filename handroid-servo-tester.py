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
while (True):
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


