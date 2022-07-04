from water_pump import WaterPump
from pigpio_dht import DHT22
from datetime import datetime
import time, sys
from plants import Plant
from LED import LED
from moisture_sensor import MoistureSensor
import write_to_iot


def main(plant: Plant):
    while True:
        try:
            result = plant.temperature_sensor.read()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_moisture = plant.get_moisture()
            f_data = f"\n\n\nCurrent Time: {current_time} - Temp: {result['temp_c']} - Humidity: {result['humidity']} - Moisture: {current_moisture}\n"
            if result["valid"] == True:
                print(f_data)
                plant.check_temperature(result["temp_c"])
                plant.check_moisture(current_moisture)
                data = {
                        "timestamp": datetime.timestamp(datetime.now()),
                        "temperature": result["temp_c"],
                        "humidity": result["humidity"],
                        "moisture": current_moisture,
                        }

                write_to_iot.write_to_iot(data)
                time.sleep(600)

        except KeyboardInterrupt:
            LED.turn_off_all_leds()
            sys.exit(0)
        except ValueError:
            continue
        except OSError:
            continue

if __name__ == "__main__":

    oregano = Plant(
        "oregano",
        humidity=(50, 90),
        temperature=(18, 24),
        moisture=(12000, 13250),
        moisture_sensor=MoistureSensor(i2c_address="0x48"),
        temperature_sensor=DHT22(17),
        green=LED(13, "green"),
        blue=LED(21, "blue"),
        red=LED(14, "red"),
        water_pump=WaterPump(27),
        secs_to_water=2
    )

    main(oregano)