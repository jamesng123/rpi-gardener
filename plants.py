import time
import RPi.GPIO as GPIO
from LED import LED
from water_pump import WaterPump
from pigpio_dht import DHT22
from moisture_sensor import MoistureSensor


class Plant:
    def __init__(
        self,
        name: str,
        humidity: tuple,
        temperature: tuple,
        moisture: tuple,
        moisture_sensor: MoistureSensor,
        temperature_sensor: DHT22,
        green: LED,
        blue: LED,
        red: LED,
        water_pump: WaterPump,
        secs_to_water: int
    ):
        self.name = name
        self.humidity = humidity
        self.temperature = temperature
        self.moisture = moisture
        self.moisture_sensor = moisture_sensor
        self.temperature_sensor = temperature_sensor
        self.green = green
        self.red = red
        self.blue = blue
        self.water_pump = water_pump
        self.secs_to_water = secs_to_water

        assert (
            temperature[0] < temperature[1]
        ), "The lower temperature threshold comes first"

        assert humidity[0] < humidity[1], "The lower humidity threshold comes first"

        assert moisture[0] < moisture[1], "The lower moisture threshold comes first"

    def check_temperature(self, current_temp: float):
        """ Checks the temperature of the plant. Performs actions to bring the temperature within a specified range """

        if self.temperature[0] <= current_temp <= self.temperature[1]:

            # This is the desired state
            print("the temperature is within range")

            # LED.turn_off_all_leds()
            # self.green.turn_on()

        elif current_temp < self.temperature[0]:

            print("This is too cold, the range is: ", self.temperature)
            self.heat_up(current_temp)
            LED.turn_off_all_leds()
            self.blue.turn_on()

        else:
            print("This is too hot, the range is: ", self.temperature)
            self.cool_down(current_temp)
            LED.turn_off_all_leds()
            self.red.turn_on()

    def check_humidity(self, current_humidity: float):
        """ Checks the humidity of the plant. Performs actions to bring the humidity within a specified range """

        if self.humidity[0] <= current_humidity <= self.humidity[1]:
            pass  # This is the desired state
        elif current_humidity < self.humidity[0]:
            # TODO Implement logic for increasing the humidity
            pass
        else:
            # TODO Implement logic for decreasing the humidity
            pass

    def check_moisture(self, current_moisture):
        """ Checks the humidity of the plant. Performs actions to bring the humidity within a specified range """

        if self.moisture[0] >= current_moisture >= self.moisture[1]:
            print("No water needed, got plenty")
            LED.turn_off_all_leds()
            self.green.turn_on()

        elif current_moisture > self.moisture[1]:
            # TODO Implement logic for watering
            print("Needs watering...")
            self.water_pump.water(self.secs_to_water)
        else:
            print("You've watered too much")

    def get_moisture(self):
        return self.moisture_sensor.get_moisture_state()

    def heat_up(self, current_temperature: float):
        """ Increases the temperature for the plant """

        # TODO Implement logic for heating up
        print("Heating up....")
        # while current_temperature < self.temperature[0]:
        #     current_temperature += 1
        #     print(current_temperature)
        #     time.sleep(1)
        #
        # print("warmed!")

    def cool_down(self, current_temperature: float):
        """ Decreases the temperature for the plant """

        # TODO Implement logic for cooling down
        print("Cooling down....")
        # while current_temperature > self.temperature[1]:
        #     current_temperature -= 1
        #     print(current_temperature)
        #     time.sleep(1)
        # print("cooled!")
