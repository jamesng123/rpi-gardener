import RPi.GPIO as GPIO
import time

class LED():

    gpio_pins = []

    def __init__(self, gpio, colour):
        self.gpio = gpio
        self.colour = colour

        # Initialse the GPIO pins and LEDs
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.gpio, GPIO.OUT)

        if self.gpio not in self.gpio_pins:
            self.gpio_pins.append(self.gpio)

    def turn_on(self):

        """ Turns on the specified LED """

        GPIO.output(self.gpio, GPIO.HIGH)
    
    def turn_off(self):

        """ Turns off the specified LED """

        GPIO.output(self.gpio, GPIO.LOW)

    @classmethod
    def turn_off_all_leds(cls):

        """ Turns off all LEDs that are currently on """

        for i in cls.gpio_pins:
            GPIO.output(i, GPIO.LOW)
