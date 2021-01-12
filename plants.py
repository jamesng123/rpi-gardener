import time
import RPi.GPIO as GPIO
import LED

class Plant():

    def __init__(self, name: str, humidity: tuple, temperature: tuple, moisture: tuple):
        self.name = name
        self.humidity = humidity
        self.temperature = temperature
        self.moisture = moisture

    def check_temperature(self, current_temp: float):
        
        """ Checks the temperature of the plant. Performs actions to bring the temperature within a specified range """

        if self.temperature[0] <= current_temp <= self.temperature[1]:

            # This is the desired state
            print("this is desired")

            LED.LED.turn_off_all_leds()
            green = LED.LED(18, "green")
            green.turn_on()

        elif current_temp < self.temperature[0]:

            print("this is too cold, the range is: ", self.temperature)
            self.heat_up(current_temp)
            
        else:
            print("this is too hot, the range is: ", self.temperature)
            self.cool_down(current_temp)
            LED.LED.turn_off_all_leds()
            red = LED.LED(23, "red")
            red.turn_on()            

    def check_humidity(self, current_humidity: float):
        if self.humidity[0] <= current_humidity <= self.humidity[1]:
            pass # This is the desired state
        elif current_humidity < self.humidity[0]:
            #TODO Implement logic for increasing the humidity
            pass
        else:
            #TODO Implement logic for decreasing the humidity
            pass

    def check_moisture(self, current_moisture: float):
        if self.moisture[0] <= current_moisture <= self.moisture[1]:
            pass # This is the desired state
        elif current_moisture < self.moisture[0]:
            #TODO Implement logic for increasing the moisture
            pass
        else:
            #TODO Implement logic for decreasing the moisture
            pass

    def heat_up(self, current_temperature):
        #TODO Implement logic for heating up
        print("heating up....")
        # while current_temperature < self.temperature[0]:
        #     current_temperature += 1
        #     print(current_temperature)
        #     time.sleep(1)
        #
        # print("warmed!")
        

    def cool_down(self, current_temperature):
        #TODO Implement logic for cooling down
        print("cooling down....")
        # while current_temperature > self.temperature[1]:
        #     current_temperature -= 1
        #     print(current_temperature)
        #     time.sleep(1)
        # print("cooled!")