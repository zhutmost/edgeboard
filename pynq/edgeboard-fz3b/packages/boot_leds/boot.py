#!/bin/env python3.6

from pynq import Overlay
from time import sleep

ol = Overlay('base.bit')
led = ol.gpio_led.channel1

for _ in range(8):
    led[0].on()
    sleep(0.2)
    led[0].off()
    sleep(0.2)


