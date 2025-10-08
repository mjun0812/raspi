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
uv run python sensor.py
```

## Send sensor value

Use crontab.

```bash
* * * * * for i in `seq 0 20 59`;do (sleep ${i}; cd /home/mjun/raspi; uv run python cron.py)& done;
```
