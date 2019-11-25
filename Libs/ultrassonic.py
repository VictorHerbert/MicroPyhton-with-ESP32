from HCSR04 import *
import time
import _thread

sensor = HCSR04(trigger_pin=5, echo_pin=18)

def ultraRead():
    while(True):
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
        time.sleep_ms(500)

_thread.start_new_thread(ultraRead, ())