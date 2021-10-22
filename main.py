
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 100)
pwm.start(0)

for dc in range(100,0):
  pwm.ChangeDutyCycle(dc)
  time.sleep(.02)

GPIO.cleanup()


