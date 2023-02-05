import requests
from datetime import datetime
import winsound
import threading

MY_LAT = 0 # add your latitude here
MY_LONG = 0 # add your longitude here

MY_POS = (MY_LAT, MY_LONG)

def get_iss_pos(): # requests the ISS position 
    r = requests.get(url="http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    data = r.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    return iss_latitude, iss_longitude


def check_overhead(): # compares your position and ISS position and noitifies you if it's night time 
    iss_latitude, iss_longitude = get_iss_pos()
    iss_near = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5  # within +/- 5 degrees


    if iss_near:
        winsound.Beep(2000, 2000)
    else:
        print(f"The ISS is currently at ({iss_latitude}, {iss_longitude}), you are at ({MY_LAT}, {MY_LONG})")


def main_function():
    threading.Timer(60.0, main_function).start()
    check_overhead()


main_function()
