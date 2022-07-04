import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class MoistureSensor:
    def __init__(self, i2c_address):

        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        self.i2c_address = i2c_address

        self.ads = ADS.ADS1115(i2c)

    def get_moisture_state(self):
        chan = AnalogIn(self.ads, ADS.P0)

        return chan.value