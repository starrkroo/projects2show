#!/bin/bash -e


# they are sinhronizing
./templates/ngrok http 4567
./code.py
