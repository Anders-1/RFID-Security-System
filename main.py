# INSTALLING:
#
# First, use the Adafruit guide to install drivers or whatever (might not be needed, but install
# the drivers anyway just to be sure).
# https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi
#
# I don't think this site installs anything, it is just example code, but if the reader isn't
# working, try following the steps in this link (after the Adafruit link of course).
# https://www.raspberrypi.com/news/read-rfid-and-nfc-tokens-with-raspberry-pi-hackspace-37/
#
# NOTE TO SELF/COMBAK: Disable alarm after long period of time (like if the door just
# randomly opens when no one is home [not sarcasm]). Also, add Cron Job to run program
# in the morning and close it at bedtime (so it isn't running at night, of course, you could
# always have it run all the time if you want). Also, check the comment/combak on line 125
# and 218. And also check todolist on google doc.

from gpiozero import LED, Button, Buzzer
import time
import datetime
from signal import pause
import threading


def info(text, severe=False):
    current_time = str(datetime.datetime.now())
    if severe:
        print("****")
        print("[IMPORTANT " + current_time + "]: " + text)
        print("****")
    else:
        print("[INFO " + current_time + "]: " + text)

# ----
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import pn532.pn532 as nfc
from pn532 import *

pn532 = PN532_UART(debug=False, reset=20)

ic, ver, rev, support = pn532.get_firmware_version()
info('Found PN532 with firmware version: {0}.{1}'.format(ver, rev), severe=True)

# Configure PN532 to communicate with NTAG215 cards
pn532.SAM_configuration()
# ----

# Variables
led1 = LED(17)
led2 = LED(24)
buzzer = Buzzer(27)
door_sensor = Button(22, pull_up=None, active_state=True)
button = Button(23)

MASTER_KEY = ['0x4', '0x3a', '0xf3', '0x38', '0xc0', '0x6d', '0x80']
GUEST_KEY = ['0x62', '0xdd', '0x6d', '0x22']

GUEST_COUNTDOWN_TIME = 20
guest_countdown = -1
safely_opened = False

start_time = 0

def blink(wait):
    led1.on()
    time.sleep(wait)
    led1.off()

def blink_green(wait):
    led2.on()
    time.sleep(wait)
    led2.off()

def beep(wait):
    buzzer.on()
    time.sleep(wait)
    buzzer.off()

def blinkandbeep(wait):
    led1.on()
    buzzer.on()
    time.sleep(wait)
    led1.off()
    buzzer.off()
    time.sleep(wait)

def blinkandbeep_green(wait):
    led2.on()
    buzzer.on()
    time.sleep(wait)
    led2.off()
    buzzer.off()
    time.sleep(wait)

def alarm(repeat):
    for _ in range(repeat):
        blinkandbeep(0.1)

def alarm_green(repeat):
    for _ in range(repeat):
        blinkandbeep_green(0.1)

def guest_countdown_handler(action = "DECREMENT"):
    global GUEST_COUNTDOWN_TIME
    global guest_countdown
    global start_time
    if action == "DECREMENT":
        start_time = time.time()
        while guest_countdown > 0:
            current_time = time.time()
            difference = current_time - start_time
            info("Guest countdown at: " + str(difference))
            if (difference % 1 > 0.9):
                blink_green(0.5)
            if difference > GUEST_COUNTDOWN_TIME:
                guest_countdown = 0
                info("Guest countdown complete")
                return
            else:
                time.sleep(0.1)
        return
    elif action == "START":
        if guest_countdown > 0:
#             COMBAK: Uncomment if you want to allow people to reset guest time
#             while the countdown is going on.

#             start_time = time.time()
            return
        guest_countdown = GUEST_COUNTDOWN_TIME
        t1 = threading.Thread(target = guest_countdown_handler, args=("DECREMENT",))
        t1.start()
#         t1.join()
        return
    elif action == "RESET":
        guest_countdown = -1
        return

def door_handler(key=None):
    global safely_opened
    global guest_countdown

    if safely_opened:
        return

    info("Door opened, getting key")
    key = get_key(3, 0.5)
    if key in [None, "NO KEY"] or guest_countdown == 0:
         if not guest_countdown > 0:
            for _ in range(10):
                if get_key(1, 0.1) == "MASTER":
                    guest_countdown_handler("RESET")
                    safely_opened = True
                    return
                else:
                    info("Alarm set off!", severe=True)
                    alarm(1)
    elif key == "MASTER":
        info("Master key opened door")
        guest_countdown_handler("RESET")
        safely_opened = True
        led2.on()
    elif key == "GUEST":
        guest_countdown_handler("START")

def get_key(attempts = 5, wait = 0.5):
    global MASTER_KEY
    global GUEST_KEY
    for _ in range(attempts):
        key = pn532.read_passive_target(timeout=wait)
        if key is not None:
            key = [hex(i) for i in key]
            if key == MASTER_KEY:
                return "MASTER"
                door_handler("MASTER")
            elif key == GUEST_KEY:
                return "GUEST"
            else:
                info("UNKNOWN KEY IS: " + str(key), severe=True)
                return "NO KEY"
        time.sleep(wait)
    return "NO KEY"

def door_close_handler():
    global safely_opened
    info("Checking if door is closed")

    key = get_key(3, 0.5)

    if door_sensor.value == 0:
        safely_opened = False
        led2.off()
        info("Door is closed")
        info("The key when closing is: " + key)
        if key not in [None, "NO KEY"]:
            guest_countdown_handler("RESET")
            info("Guest_Countdown after reset is: " + str(guest_countdown))

def button_handler():
    key = get_key(2, 0.1)
    info("Button pressed. Key is: " + key)
    if key == "MASTER":
        blink_green(0.5)
    elif key == "GUEST":
        blink_green(0.5)
        time.sleep(0.5)
        blink_green(0.5)
    else:
        blink(0.5)

def button_new_thread():
    t2 = threading.Thread(target = button_handler)
    t2.start()

door_sensor.when_pressed = door_handler
door_sensor.when_released = door_close_handler

# COMBAK: Comment this out if people pressing the button is causing problems.
button.when_pressed = button_new_thread

pause()
