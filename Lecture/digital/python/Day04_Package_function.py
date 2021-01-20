# 매개변수x , 리턴값 x
def printcoins():
    print('bitcoin')

# 매개변수x , 리턴값o
def returnfunc() :
    return '호출한 쪽으로 값이 전달'

# 매개변수o , 리턴값o
def sayecho(name) :
    return name + " 님, 반갑습니다!"

def calculator(op01,op02,op03) :
    pass

def makeurl(url) :
    return "www."+url+".com"

# 매개변수o , 리턴값x
def badfunc(name) :
    pass

#####
def tuplefunc(*args) :
    result = 0
    for idx in range(len(args)) :
        result += args[idx]
    return result

def dictfunc(**args) :
    for key, value in args.items() :
        print('{}={}'.format(key , value))

# 범위내에 있는 홀,짝의 합
def cntsum(start , end) :
    odd = even = 0
    for x in range(start , end+1) :
        if x%2== 0 :
            even += x
        else :
            odd += x
    return (odd, even)

def leapyearfunc(startyear , endyear) :
    yearlist = []
    for year in range(startyear , endyear+1) :
        if (year%4 == 0 and year%100 != 0 ) or (year%400 == 0) :
            yearlist.append(year)
    return yearlist

def rtndictfunc(x) :
    y01 = x * 10
    y02 = x * 20
    y03 = x * 30
    return {'val01':y01 , 'val02':y02 , 'val03':y03}