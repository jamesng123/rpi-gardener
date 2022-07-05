import RPi.GPIO as GPIO
import time

class WaterPump():

    def __init__(self, gpio: int):
        self.gpio = gpio

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)
        GPIO.output(self.gpio, GPIO.HIGH)


    def water(self, seconds):
        GPIO.output(self.gpio, GPIO.LOW)
        time.sleep(seconds)
        GPIO.output(self.gpio, GPIO.HIGH)
