import simpleaudio as sa
import time as tm

mysound="a1.wav"
wave_obj = sa.WaveObject.from_wave_file(mysound)


def countdown(time,factor):
    sec=0
    time=int(time)
    if (factor=='s'):
        sec=time
    elif(factor=='m'):
        sec=time*60
    elif(factor=='h'):
        sec=time*60*60
    else:
        print("invalid factor")

    print("sleeping for "+str(sec)+" secs")
    tm.sleep(int(sec))
    play_obj = wave_obj.play()
    play_obj.wait_done()

def alarm(time):
    timer=time.split(":")
    timeh=timer[0]
    timem=timer[1]
    print ("will ring at "+timeh+" hours and "+timem+" mins")
    while True:
        timenow = tm.localtime()
        if timenow.tm_hour==int(timeh) and timenow.tm_min==int(timem):
            play_obj = wave_obj.play()
            play_obj.wait_done()
            print ("sounded")
            break


alarm_type=int(input("Alarm Type:\n"
                     "1:Countdown Timer\n"
                     "2:Alarm Clock(cant kill program to sound)\n"
                     "please input your choice:"))


if alarm_type==1:
    timein=input("countdown time \n"
                 "(10s for 10 sec 10m for 10 min and 10h for 10 hours):\n")
    time=timein[0:-1]
    time_factor=timein[-1]
    if len(time_factor)!=1 or time_factor.isnumeric():
        exit("invalid time")
    countdown(time,time_factor)
elif alarm_type==2:
    timein=input("ring when (HH:MM)(24h): ")
    alarm(timein)
else:
    print("invalid input")

