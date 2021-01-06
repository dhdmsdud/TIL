# python date type
from datetime import date , datetime
today = date.today
print(today , type(today) , today)

# 시간
todaydatetime = datetime.today()
print(todaydatetime)
print('시{}' , '분 {}' , '초 {}'.format(todaydatetime.hour , todaydatetime.minute , todaydatetime.microsecond))

# dateutil
# install
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

today = date.today()
days = timedelta(days=-1)
print(today)
print('오늘 이전 하루 - {}'.format(today+days))

# year ,  month 관련된 옵션 relativedelte
days = relativedelta(months=-2)
print('두달 전 오늘 - {}'.format(today+days))
days = relativedelta(years=-1)
print('일년 전 오늘 - {}'.format(today+days))

# parse
from dateutil.parser import parse
userdate = parse("2021-06-04")
print(userdate , type(userdate))
userdate = datetime(2021, 12, 25)
print(userdate , type(userdate))

# 날짜 객체의 출력형식을 원하는것으로 변경
# 날짜형식 -> 문자열형식으로 포맷 : strftime
today = datetime.today()
print("{}".format(today.strftime('%m-%d-%Y'))) # 2021
print("{}".format(today.strftime('%m-%d-%y'))) #21

# 문자열형식 -> 날짜형식 : strptype
strdate = '2021,01,06-11:12:40'
userdate = datetime.strptime(strdate , '%Y,%m,%d-%H:%M:%S')
print(type(userdate) , userdate)
