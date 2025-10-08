import os
import sys
import fcntl

import cgsensor
import mh_z19
import requests
from requests.exceptions import Timeout
from dotenv import load_dotenv

_LOCK_FILE = "/tmp/sensor.pid"
_lock_fp = None


def _acquire_lock():
    global _lock_fp
    _lock_fp = open(_LOCK_FILE, "w")
    try:
        # 非ブロッキング排他ロックを取得
        fcntl.flock(_lock_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("The script's process is already existed")
        sys.exit(1)

    _lock_fp.write(str(os.getpid()))
    _lock_fp.flush()


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

    result["co2"] = mh_z19.read(serial_console_untouched=True).get("co2")
    return result


def main():
    _acquire_lock()
    load_dotenv()
    post_url = os.getenv("POST_URL")
    try:
        payload = get_sensor_info()
        requests.post(post_url, json=payload, timeout=(5, 30))
    except Timeout:
        print("Timeout")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
