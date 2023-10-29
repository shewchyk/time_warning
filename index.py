# just for fun, audible countdown to calendar appointments starting
# should play an audio file at speific times to a calendar i.e. "60 seconds" will play 1 min before a meeting

from playsound import playsound
import datetime
from datetime import datetime, date

warnings = ['/home/andrew/code/time_warning/10mins.mp3','/home/andrew/code/time_warning/5mins.mp3','/home/andrew/code/time_warning/3mins.mp3','/home/andrew/code/time_warning/90secs.mp3','/home/andrew/code/time_warning/60secs.mp3','/home/andrew/code/time_warning/30secs.mp3','/home/andrew/code/time_warning/10secs.mp3','/home/andrew/code/time_warning/goinglive.mp3']

meeting_time = datetime(2023, 10, 24, 8, 30, 00)
timenow = datetime.now()
trigger = meeting_time - timenow

sec_trigger = round(trigger.total_seconds())

print(meeting_time)
print(sec_trigger)

def test(seconds):
    if seconds == 3:
        playsound(warnings[7])
    elif seconds == 10:
        playsound(warnings[6])
    elif seconds == 30:
        playsound(warnings[5])
    elif seconds == 60:
        playsound(warnings[4])
    elif seconds == 90:
        playsound(warnings[3])
    elif seconds == 180:
        playsound(warnings[2])
    elif seconds == 300:
        playsound(warnings[1])
    elif seconds == 600:
        playsound(warnings[0])
    else: pass

test(sec_trigger)