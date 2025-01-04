# My Raspberry Pi Zero 2 W repository

## Install

```bash
./setup.sh
```

## Sensor

- BME280: temperature, humidity, air pressure
- TSL2572: Brightness
- MH-Z19C: CO2

```bash
sudo python sensor.py
```

## Send sensor value

Use crontab.

```bash
* * * * * for i in `seq 0 5 59`;do (sleep ${i}; cd /home/mjun/raspi; /home/mjun/.venv/bin/python cron.py)& done;
```
