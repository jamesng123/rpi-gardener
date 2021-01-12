import RPi.GPIO as GPIO
import time

class LED():

    GPIO_PINS = []

    def __init__(self, GPIO_PIN, colour):
        self.GPIO_PIN = GPIO_PIN
        self.colour = colour

        # Initialse the GPIO pins and LEDs
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.GPIO_PIN, GPIO.OUT)

        if self.GPIO_PIN not in self.GPIO_PINS:
            self.GPIO_PINS.append(self.GPIO_PIN)

    def turn_on(self):
        GPIO.output(self.GPIO_PIN, GPIO.HIGH)
    
    def turn_off(self):
        GPIO.output(self.GPIO_PIN, GPIO.LOW)

    @classmethod
    def turn_off_all_leds(cls):
        for i in cls.GPIO_PINS:
            GPIO.output(i, GPIO.LOW)
