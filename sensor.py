import cgsensor
import mh_z19
from pprint import pprint


def main():
    result = {}

    bme280 = cgsensor.BME280(i2c_addr=0x76)
    bme280.forced()
    result["温度"] = bme280.temperature
    result["湿度"] = bme280.humidity
    result["気圧"] = bme280.pressure

    tsl2572 = cgsensor.TSL2572()
    tsl2572.single_auto_measure()
    result["照度"] = tsl2572.illuminance

    result["CO2"] = mh_z19.read()["co2"]

    pprint(result)


if __name__ == "__main__":
    main()
