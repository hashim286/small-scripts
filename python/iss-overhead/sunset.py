import requests
from datetime import datetime
import winsound
import threading

MY_LAT = 0 # add your latitude here
MY_LONG = 0 # add your longitude here

MY_POS = (MY_LAT, MY_LONG)



def get_sun_times():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0
    }
    r = requests.get("https://api.sunrise-sunset.org/json", params=parameters) # requests sunrise and sunset times based on your latitude and longitude
    r.raise_for_status()
    data = r.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) # isolates the hours for sunrise and sunset times
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    
    return sunrise, sunset




def get_iss_pos(): # requests the ISS position 
    r = requests.get(url="http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    data = r.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    return iss_latitude, iss_longitude

def check_overhead(): # compares your position and ISS position and noitifies you if it's night time 
    iss_latitude, iss_longitude = get_iss_pos()
    sunrise, sunset = get_sun_times()

    timenow = datetime.now()

    current_hour = timenow.hour

    iss_near = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5  # within +/- 5 degrees
    is_it_dark = current_hour >= sunset or current_hour <= sunrise # checks if it's between sunset and sunrise



    if iss_near and is_it_dark:
        winsound.Beep(2000, 2000)
    else:
        print(f"The ISS is currently at ({iss_latitude}, {iss_longitude}), you are at ({MY_LAT}, {MY_LONG})")
        print(f"Current hour is {current_hour}, sunrise hour is {sunrise}, sunset hour is {sunset}")

def main_function():
    threading.Timer(60.0, main_function).start()
    check_overhead()


main_function()
