from datetime import datetime
import pytz

# getting utc time, without defining time-zones
current_utc_time = datetime.utcnow()
print('utc time, no time zone: ',current_utc_time)

# defining time zones
utc_zone = pytz.utc
ist_zone = pytz.timezone('Asia/Kolkata')

# putting utc time zone to time
current_utc_time = current_utc_time.replace(tzinfo=utc_zone)
print('utc time, time zone included: ', current_utc_time)

#putting ist time zine to time
current_ist_time = current_utc_time.astimezone(ist_zone)
print('cur time, shown as-time-zone ist: ' ,current_ist_time)

# printing time in different format using, strftime
print('y-m-d h-m-s tz format: ', current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print('d-m-y tz format: ', current_ist_time.strftime('%d.%m.%Y %Z%z'))
