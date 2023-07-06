#!/bin/bash

sudo apt update && sudo apt install -y vim pip

sudo pip install -r requirements.txt

sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_vnc 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial 0

