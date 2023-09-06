## %a	                                 Weekday, short version	
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%a"))
'''

## %A	                                 Weekday, full version
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%A"))
'''

## %w	                                 Weekday as a number 0-6, 0 is Sunday
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%w"))
'''

## %d	                                 Day of month 01-31
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%d"))
'''

## %b	                                 Month name, short version
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%b"))
'''

## %B	                                Month name, full version
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%B"))
'''

## %m	                                 Month as a number 01-12
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%m"))
'''

## %y	                                 Year, short version, without century
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%y"))
'''

## %Y	                                 Year, full version
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%Y"))
'''

## %H	                                 Hour 00-23
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%H"))
'''

## %I	                                 Hour 00-12
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%I"))
'''

## %p	                                 AM/PM
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%p"))
'''

## %M	                                 Minute 00-59
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%M"))
'''

## %S	                                 Second 00-59
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%S"))
'''

## %f	                                 Microsecond 000000-999999
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%f"))
'''

## %z	                                 UTC offset
'''
import datetime

# Create a datetime object with a specific UTC offset
dt = datetime.datetime(2023, 4, 7, 14, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

# Format the UTC offset using %z
formatted_utc_offset = dt.strftime("%z")

print(formatted_utc_offset)  # Output: "+0530"
'''

## %Z	                                 Timezone
'''
pass
'''

## %j	                                 Day number of year 001-366
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%j"))
'''

## %U	                                 Week number of year,Sunday as the first day of week, 00-53
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%U"))
'''

## %W	                                 Week number of year,Monday as the first day of week, 00-53
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%W"))
'''

## %c	                                 Local version of date and time	Mon Dec 31 17:41:00
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%c"))
'''

## %C	                                 Century
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%C"))
'''

## %x	                                 Local version of date
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%x"))
'''

## %X	                                 Local version of time
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%X"))
'''

## %%	                                 A % character
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%%"))
'''

## %G	                                 ISO 8601 year
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%G"))
'''

## %u	                                 ISO 8601 weekday (1-7)
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%u"))
'''

## %V	                                 ISO 8601 weeknumber (01-53)
'''
import datetime

x = datetime.datetime.now()
print(x.strftime("%V"))
'''