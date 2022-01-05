# Author: Dante Sivo
# Date Created: 12/19/2021
''' Description: Calibration of daylight simulated to time entered. 
        Time entered must be in 24-hour standard (EST).    
'''
from datetime import tzinfo, timedelta, datetime

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(hours=offset)
        self.__dst = timedelta(hours=offset-1)
        self.__name = ''

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return self.__dst

# Dictonary of standard timezones. Offset to GMT
timezone_dict = {
    "PST": -8 ,
    "MST": -7 ,
    "CST": -6,
    "EST": -5,
    "GMT": 0,
    "CST": 8,
    "JST": 9,
    "AEDT": 11,
    "NZDT": 13
}


''' get_current_time
Description : Helper function to get current time based on timezone initals
                or fixed offset value
'''
def get_current_time(timezone = 'NA', offset = 24):
    if (offset != 24):  # If numerical offset was specified
        return datetime.now(FixedOffset(offset))
    elif timezone in timezone_dict: # Otherwise, check for timezone value
        return timezone_dict.value(timezone)
    else:
        return datetime.now() # If no parameters given. Get system timezone
        

print(timezone_dict.keys())
print(timezone_dict.values())
alarm = datetime.now()
alarm = alarm.replace(hour = 7, minute = 30)
alarm = get_current_time(-5)
dd = datetime.now(FixedOffset(-5))
print("Current " +  str(dd.hour) + ":" + str(dd.minute) + ":" + str(dd.second))
print("Func: " + str(alarm.hour) + ":" + str(alarm.minute) + ":" + str(alarm.second))
