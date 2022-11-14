import os
import cgsensor
import mh_z19
import requests
from dotenv import load_dotenv


def get_sensor_info():
    result = {}

    bme280 = cgsensor.BME280(i2c_addr=0x76)
    bme280.forced()
    result["temp"] = bme280.temperature
    result["humid"] = bme280.humidity
    result["pressure"] = bme280.pressure

    tsl2572 = cgsensor.TSL2572()
    tsl2572.single_auto_measure()
    result["brightness"] = tsl2572.illuminance

    result["co2"] = mh_z19.read()["co2"]
    return result


def main():
    load_dotenv()
    post_url = os.getenv("POST_URL")
    response = requests.post(post_url, json=get_sensor_info())
    print(response.status_code)


if __name__ == "__main__":
    main()
