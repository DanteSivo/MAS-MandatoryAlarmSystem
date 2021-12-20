# Author: Dante Sivo
# Date Created: 12/19/2021
''' Description: Calibration of daylight simulated to time entered. 
        Time entered must be in 24-hour standard (EST).    
'''
from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))
