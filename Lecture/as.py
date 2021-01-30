from statistics import *

mpgList = []
with open('./word/mpg.txt' , 'r') as file :
    file.readline()
    line = file.readline()
    while line != '' :
        data = line.strip('\n').split(',')
        obj = m.Mpg(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])
        mpgList.append(obj)
        line = file.readline()



# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

def question01():
    displ04 = []
    displ05 = []
    for instance in mpgList :
        if float(instance.getDispl()) <= 4 :
            displ04.append(int(instance.getHwy()))
        if float(instance.getDispl()) >= 5 :
            displ05.append(int(instance.getHwy()))
    print('4 - ' , mean(displ04))
    print('5 - ' , mean(displ05))
    disp4_mean = mean(displ04)
    disp5_mean = mean(displ05)

    if displ04 > displ05 :
        print('배기량 4의 연비가 더 좋습니다.')
    else :
        print('배기량 5의 연비가 더 좋습니다.')
# question01()

# from statistics import mean
# with open('./word/mpg.txt','r', encoding = 'utf-8') as file:
#     file.readline()
#     line=file.readline()
#     cyl4 = []
#     cyl5 = []
#     while line != '':
#         data = line.strip('\n').split(',')
#         if float(data[2]) <= 4:
#             cyl4.append(int(data[8]))
#         if float(data[2]) >=5:
#             cyl5.append(int(data[8]))
#         line=file.readline()
#     print(mean(cyl4))
#     print(mean(cyl5))
#     if(mean(cyl4)>mean(cyl5)):
#         print('4 is bigger')
#     else:
#         print('5 is bigger')






# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.
def question02() :
    audi = []
    toyota = []
    for instance in mpgList:
        if instance.getManufacturer() =='audi':
            audi.append(int(instance.getCty()))
        if instance.getManufacturer() == 'toyota':
            toyota.append(int(instance.getCty()))
    if mean(audi) > mean(toyota):
        print('audi가 연비가 높습니다.')
    else:
        print('toyota가 연비가 높습니다.')
# question02()


# with open('./word/mpg.txt','r', encoding = 'utf-8') as file:
#     file.readline()
#     line=file.readline()
#     audi = []
#     toyota = []
#     while line != '':
#         data = line.strip('\n').split(',')
#         audi.append(int(data[7]))
#         toyota.append(int(data[7]))
#         line=file.readline()
#     print(mean(audi))
#     print(mean(toyota))
#     if(mean(audi)>mean(toyota)):
#         print('audi is bigger')
#     else:
#         print('toyota is higher')

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

def question03() :
    chevrolet = []
    ford = []
    honda = []
    for instance in mpgList:
        if instance.getManufacturer() == 'chevrolet':
            chevrolet.append(int(instance.getHwy()))
        if instance.getManufacturer() == 'ford' :
            ford.append(int(instance.getHwy()))
        if instance.getManufacturer() == 'honda' :
            honda.append(int(instance.getHwy()))
    print('쉐보레의 평균: ',mean(chevrolet))
    print('포드의 평균: ', mean(ford))
    print('혼다의 평균: ', mean(honda))
# question03()


# with open('./word/mpg.txt','r', encoding = 'utf-8') as file:
#     file.readline()
#     line = file.readline()
#     chevrolet =[]
#     ford = []
#     honda =[]
#     while line != '':
#         data = line.strip('\n').split(',')
#         chevrolet.append(int(data[-3]))
#         ford.append(int(data[-3]))
#         honda.append(int(data[-3]))
#         line= file.readline()
#     print('쉐보레',mean(chevrolet))
#     print('포드',mean(ford))
#     print('혼다',mean(honda))


# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.
def question04():
    audi_list = []
    for i in mpgList:
        if i.getManufacturer() == 'audi':
            audi_list.append(i)
    audi_list.sort(key=lambda object : object.getHwy(), reverse=True)
    for i in range(5) :
        print("model {} , hwy {} ".format(audi_list[i].getModel(),audi_list[i].getHwy()))
# question04()


# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.
def question05() :

    suv_list = []
    manu_over_sum = {}
    manu_cnt = {}



    for instance in mpgList:
        instance.overall = (float(instance.getCty()) + float(instance.getHwy()))/2

    for instance in mpgList :
        # instance.overall = (float(instance.getCty()) + float(instance.getHwy())) / 2
        if instance.getCls() == 'suv' :
            manu_over_sum[instance.getManufacturer()] = manu_over_sum.get(instance.getManufacturer(), 0) + instance.overall
            manu_cnt[instance.getManufacturer()] = manu_cnt.get(instance.getManufacturer(), 0) + 1

    # { chevrolet : 0 }
    print(manu_over_sum)
    print(manu_cnt)

    for i in manu_over_sum.keys() :
        # print(i)
        suv_list.append([i, round(manu_over_sum[i] / manu_cnt[i], 2)])

    print(suv_list)

    suv_list.sort(key=lambda object: object[1], reverse=True)
    print(suv_list[0:5])

# question05()






# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

def question06() :
    list = []
    cty_sum = {}
    class_cnt = {}

    for i in mpgList:
        cty_sum[i.getCls()] = cty_sum.get(i.getCls(),0) + int(i.getCty())
        class_cnt[i.getCls()] = class_cnt.get(i.getCls(), 0) + 1
    for i in cty_sum.keys():
        list.append([i, round(cty_sum[i]/class_cnt[i],2)])
    list.sort(key=lambda object: object[1], reverse=True)
    print(list)
#question06()

# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

def question07():
    hwy_sum = {}
    class_cnt = {}
    list = []

    for i in mpgList:
        hwy_sum[i.getManufacturer()] = hwy_sum.get(i.getManufacturer(),0) + int(i.getHwy())
        class_cnt[i.getManufacturer()] = class_cnt.get(i.getManufacturer(),0) + 1
    for i in hwy_sum.keys():
        list.append([i, round(hwy_sum[i]/class_cnt[i],2)])
        list.sort(key=lambda object: object[1], reverse=True)
    print(list[0:3])
# question07()

# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
def question08() :
    manu_cnt = {}

    for i in mpgList:
        if i.getCls()=='compact':
            manu_cnt[i.getManufacturer()] = manu_cnt.get(i.getManufacturer(),0) + 1
    manu_cnt= sorted(manu_cnt.items(),key=lambda x: x[1], reverse=True)
    print(manu_cnt)
question08()


file = open("./word/mpg.txt","r")
car_list = list()
line = file.readline()
while True:
    line = file.readline()
    if not line:
        break
    car_list.append(Car(line.strip()))
file.close()