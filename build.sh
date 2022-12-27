#!/usr/bin/env bash
# exit on error
set -o errexit
sudo apt install portaudio19-dev python-pyaudio
pip install --upgrade pip
pip install -r requirements.txt