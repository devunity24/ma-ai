import time
import pytz
from datetime import datetime

class TimeUtil:
    
    timezone = pytz.timezone(time.tzname[time.daylight])
    localTimezone = timezone.localize(datetime.now())
    timeFormat = '%H:%M:%S %Z%z'
    dateFormat = '%Y-%m-%d'
    dateTimeFormat = '%Y-%m-%d %H:%M:%S %Z%z'

    @staticmethod
    def getCurrentTimeInMillies():
        return int(time.time() * 1000)

    @staticmethod
    def getFormattedTime():
        return TimeUtil.localTimezone.strftime(TimeUtil.timeFormat)

    @staticmethod
    def getFormattedDate():
        return TimeUtil.localTimezone.strftime(TimeUtil.dateFormat)

    @staticmethod
    def getFormattedDateTime():
        return TimeUtil.localTimezone.strftime(TimeUtil.dateTimeFormat)
