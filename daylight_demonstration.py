# Author: Dante Sivo
# Date Created: 12/19/2021
''' Description: Calibration of daylight simulated to time entered. 
        Time entered must be in 24-hour standard (EST).    
'''

from datetime import datetime, timezone

while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
