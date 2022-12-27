#!/usr/bin/env bash
# exit on error
set -o errexit
pip install PyAudio-0.2.11-cp37-cp37m-win32.whl
pip install --upgrade pip
pip install -r requirements.txt