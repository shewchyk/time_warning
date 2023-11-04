# just for fun, audible countdown to calendar appointments starting
# should play an audio file at speific times to a calendar i.e. "60 seconds" will play 1 min before a meeting

from playsound import playsound
import datetime
from datetime import datetime, date
import time

warnings = ['/home/andrew/code/time_warning/10mins.mp3','/home/andrew/code/time_warning/5mins.mp3','/home/andrew/code/time_warning/3mins.mp3','/home/andrew/code/time_warning/90secs.mp3','/home/andrew/code/time_warning/60secs.mp3','/home/andrew/code/time_warning/30secs.mp3','/home/andrew/code/time_warning/10secs.mp3','/home/andrew/code/time_warning/goinglive.mp3']

while True:
 meeting_time = datetime(2023, 11, 4, 7, 35, 00)
 timenow = datetime.now()
 trigger = meeting_time - timenow

 sec_trigger = round(trigger.total_seconds())


 print(meeting_time)
 print(sec_trigger)

 def test(seconds):
    if seconds < 3 and seconds > 0:
        playsound(warnings[7])
    elif seconds < 12 and seconds > 8:
        playsound(warnings[6])
    elif seconds < 32 and seconds > 28:
        playsound(warnings[5])
    elif seconds < 62 and seconds > 58:
        playsound(warnings[4])
    elif seconds < 92 and seconds > 88:
        playsound(warnings[3])
    elif seconds < 182 and seconds > 178:
        playsound(warnings[2])
    elif seconds < 302 and seconds > 298:
        playsound(warnings[1])
    elif seconds < 602 and seconds > 598:
        playsound(warnings[0])
    else: pass


 test(sec_trigger)  
 time.sleep(2)
 if sec_trigger < 0:
     break        