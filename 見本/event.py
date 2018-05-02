#!/usr/bin/python -u
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time

### 設定
PIN_L_1 = 22
PIN_L_2 = 27
PIN_L_3 = 17
PIN_R_1 = 23
PIN_R_2 = 24
PIN_R_3 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_L_1, GPIO.IN)
GPIO.setup(PIN_L_2, GPIO.IN)
GPIO.setup(PIN_L_3, GPIO.IN)
GPIO.setup(PIN_R_1, GPIO.IN)
GPIO.setup(PIN_R_2, GPIO.IN)
GPIO.setup(PIN_R_3, GPIO.IN)


status_l_1 = 0
status_l_2 = 0
status_l_3 = 0
status_r_1 = 0
status_r_2 = 0
status_r_3 = 0

### ヘッダ
print("Content-Type: text/event-stream")
print("Connection: close")
print("")

while True:
    print("event: heartbeat")
    print("data: alive")
    print("")

    # Left
    value_l_1 = GPIO.input(PIN_L_1)
    if value_l_1 != status_l_1:
        print("event: touch_l1")
        print('data: ' + str(value_l_1))
        print("")
        status_l_1 = value_l_1

    value_l_2 = GPIO.input(PIN_L_2)
    if value_l_2 != status_l_2:
        print("event: touch_l2")
        print('data: ' + str(value_l_2))
        print("")
        status_l_2 = value_l_2

    value_l_3 = GPIO.input(PIN_L_3)
    if value_l_3 != status_l_3:
        print("event: touch_l3")
        print('data: ' + str(value_l_3))
        print("")
        status_l_3 = value_l_3

    # Right
    value_r_1 = GPIO.input(PIN_R_1)
    if value_r_1 != status_r_1:
        print("event: touch_r1")
        print('data: ' + str(value_r_1))
        print("")
        status_r_1 = value_r_1

    value_r_2 = GPIO.input(PIN_R_2)
    if value_r_2 != status_r_2:
        print("event: touch_r2")
        print('data: ' + str(value_r_2))
        print("")
        status_r_2 = value_r_2

    value_r_3 = GPIO.input(PIN_R_3)
    if value_r_3 != status_r_3:
        print("event: touch_r3")
        print('data: ' + str(value_r_3))
        print("")
        status_r_3 = value_r_3

    time.sleep(0.5)

GPIO.cleanup()
