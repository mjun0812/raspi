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
* * * * *  cd /home/mjun/workspace/raspi && /usr/bin/python cron.py
```
