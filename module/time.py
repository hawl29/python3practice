import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt_dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    re_tz = re.compile(r'(UTC)(\+\d+|-\d+):\d+')
    tz_hour = int(re_tz.match(tz_str).group(2))
    tz_utc_x= timezone(timedelta(hours=tz_hour))
    dt_new_tz = dt_dt.replace(tzinfo=tz_utc_x)
    return dt_new_tz.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
