# just for fun, audible countdown to calendar appointments starting
# should play an audio file at speific times to a calendar i.e. "60 seconds" will play 1 min before a meeting

from playsound import playsound
import datetime
from datetime import datetime, date
import time

warnings = ['/home/andrew/code/time_warning/10mins.mp3','/home/andrew/code/time_warning/5mins.mp3','/home/andrew/code/time_warning/3mins.mp3','/home/andrew/code/time_warning/90secs.mp3','/home/andrew/code/time_warning/60secs.mp3','/home/andrew/code/time_warning/30secs.mp3','/home/andrew/code/time_warning/10secs.mp3','/home/andrew/code/time_warning/goinglive.mp3']

while True:
 meeting_time = datetime(2023, 11, 4, 18, 0, 00)
 timenow = datetime.now()
 trigger = meeting_time - timenow

 sec_trigger = round(trigger.total_seconds())

 def audio_clip(seconds):
    if seconds == 3:
        playsound(warnings[7])
        print(sec_trigger)
    elif seconds == 10:
        playsound(warnings[6])
        print(sec_trigger)
        time.sleep(1)
    elif seconds == 30:
        playsound(warnings[5])
        print(sec_trigger)
        time.sleep(15)
    elif seconds == 60:
        playsound(warnings[4])
        print(sec_trigger)
        time.sleep(25)
    elif seconds == 90:
        playsound(warnings[3])
        print(sec_trigger)
        time.sleep(25)
    elif seconds == 180:
        playsound(warnings[2])
        print(sec_trigger)
        time.sleep(85)
    elif seconds == 300:
        playsound(warnings[1])
        print(sec_trigger)
        time.sleep(115)
    elif seconds == 600:
        playsound(warnings[0])
        print(sec_trigger)
        time.sleep(295)
#Below lines "filter" the countdown into the set times, it saves the CPU a lot of work
    elif seconds <= 610 and seconds >= 601:
        print(sec_trigger)
        time.sleep(1)
    elif seconds < 680 and seconds >= 611:
        print(sec_trigger)
        time.sleep(10)
    elif seconds < 859 and seconds >= 681:
        print(sec_trigger)
        time.sleep(60)
    elif seconds > 860:
        print(sec_trigger)
        time.sleep(180)
    else: 
        print("Som din' fuk'd up")
        time.sleep(1)

 audio_clip(sec_trigger)  
 if sec_trigger < 0:
     break        