import os

import cgsensor
import mh_z19
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout
from dotenv import load_dotenv


def get_sensor_info():
    result = {}

    bme280 = cgsensor.BME280(i2c_addr=0x76)
    bme280.forced()
    result["temperature"] = bme280.temperature
    result["humidity"] = bme280.humidity
    result["air_pressure"] = bme280.pressure

    tsl2572 = cgsensor.TSL2572()
    tsl2572.single_auto_measure()
    result["brightness"] = tsl2572.illuminance

    result["co2"] = mh_z19.read()["co2"]
    return result


def main():
    load_dotenv()
    post_url = os.getenv("POST_URL")
    user = os.getenv("BASIC_USER")
    password = os.getenv("BASIC_PASS")
    try:
        response = requests.post(
            post_url,
            json=get_sensor_info(),
            auth=HTTPBasicAuth(username=user, password=password),
            timeout=(5, 30)
        )
        print(response.status_code)
    except Timeout:
        print("Timeout")


if __name__ == "__main__":
    main()
