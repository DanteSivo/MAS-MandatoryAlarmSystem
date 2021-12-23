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

alarm = datetime.now()
alarm = alarm.replace(hour = 7, minute = 30)
dd = datetime.now(FixedOffset(-5))
print(str(dd.hour) + ":" + str(dd.minute) + ":" + str(dd.second))
