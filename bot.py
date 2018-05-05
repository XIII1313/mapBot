import time
import os
import datetime


def get_current_time():
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)

    if len(minute) == 1:
        minute = "0" + minute

    if len(hour) == 1:
        hour = "0" + hour
    time = "{}:{}".format(hour, minute)
    
    return time


def main():
    
    var_one = os.environ.get('var_one', None)
    
    try:
        print("start")
        print(var_one)
        print("succeeded")
        print(get_current_time())
        time.sleep(20)
        main()
        
    except:
        print("error")
        time.sleep(5)
        print("restarting")
        main()


main()
