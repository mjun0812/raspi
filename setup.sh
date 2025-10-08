#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install -y vim curl swig liblgpio-dev

sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_vnc 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial 0

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

uv sync
uv run cgsensor all
uv run python -m mh_z19 --serial_console_untouched

