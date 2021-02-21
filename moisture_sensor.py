import RPi.GPIO as GPIO

class MoistureSensor():

    def __init__(self, gpio):
        self.gpio = gpio

        # Initialse the GPIO pins and LEDs
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.gpio, GPIO.IN)

    def get_moisture_state(self):

        """ Returns True if the plant needs water and False if not """

        if GPIO.input(self.gpio):
            return True
        else:
            return False