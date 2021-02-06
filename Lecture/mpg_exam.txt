from statistics import *

def load_data():
    with open(file="./word/mpg.txt", mode="r", encoding="utf8") as file:
        features = file.readline().split(",")
        # print("debug : ", features)
        car_list = []
        for line in file.readlines():
            car = line.split(",")
            dic = {}
            for idx in range(len(car)):
                dic[features[idx]] = car[idx]
            car_list.append(dic)
            print("debug : ", car_list)
    return car_list

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
hwy_displ4 = hwy_displ5 = 0
count_displ4 = count_displ5 = 0

with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if float(car_info[2]) <= 4:
            hwy_displ4 += int(car_info[-3])
            count_displ4 += 1
        if float(car_info[2]) >= 5:
            hwy_displ5 += int(car_info[-3])
            count_displ5 += 1

print('배기량 4 이하 자동차의 고속도로 연비 평균 : {}'.format(hwy_displ4 / count_displ4))
print('배기량 5 이상 자동차의 고속도로 연비 평균 : {}'.format(hwy_displ5 / count_displ5))

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.
cty_audi = cty_toyota = 0
count_audi = count_toyota = 0

with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[0] == 'audi':
            cty_audi += int(car_info[-4])
            count_audi += 1
        if car_info[0] == 'toyota':
            cty_toyota += int(car_info[-4])
            count_toyota += 1

print('audi의 도시 연비 평균 : {}'.format(cty_audi / count_audi))
print('toyota의 도시 연비 평균 : {}'.format(cty_toyota / count_toyota))
# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
hwy_chevrolet = hwy_ford = hwy_honda = 0
count_chevrolet = count_ford = count_honda = 0

with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[0] == 'chevrolet':
            hwy_chevrolet += int(car_info[-3])
            count_chevrolet += 1
        if car_info[0] == 'ford':
            hwy_ford += int(car_info[-3])
            count_ford += 1
        if car_info[0] == 'honda':
            hwy_honda += int(car_info[-3])
            count_honda += 1

print('chevrolet의 고속도로 연비 평균 : {}'.format(hwy_chevrolet / count_chevrolet))
print('ford의 고속도로 연비 평균 : {}'.format(hwy_ford / count_ford))
print('honda의 고속도로 연비 평균 : {}'.format(hwy_honda / count_honda))
# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요. sort사용
audi_list = []

with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[0] == 'audi':
            audi_list.append(car_info)

audi_cars = sorted(audi_list, key=lambda c: c[-3], reverse=True)
for i in range(5):
    print(audi_list[i])
# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.
car_list = []

with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        mpg_data = (int(car_info[-4]) + int(car_info[-3])) / 2
        car_info.append(mpg_data)
        car_list.append(car_info)

suv_avg = []
suv_count = []
for car in car_list:
    if car[-2] == 'suv':
        if car[0] not in suv_avg:
            suv_avg.append(car[0])
            suv_count.append([car[-1], 1])
        else:
            suv_count[-1][0] += car[-1]
            suv_count[-1][1] += 1

suv_mpg_data = [data[0]/data[1] for data in suv_count]
suv_mpg_avg = tuple(zip(suv_avg, suv_mpg_data))
suv_mpg_avg = sorted(suv_mpg_avg, key=lambda data: data[1], reverse=True)
for i in range(5):
    print('제조사 : {} 고속도로와 도시 연비의 평균 : {}'.format(suv_mpg_avg[i][0], suv_mpg_avg[i][1]))
# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.
car_class = []
car_cty = []
with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[-1] not in car_class:
            car_class.append(car_info[-1])
            car_cty.append([int(car_info[-4]), 1])
        else:
            index = car_class.index(car_info[-1])
            car_cty[index][0] += int(car_info[-4])
            car_cty[index][1] += 1

car_class_cty01 = [data[0]/data[1] for data in car_cty]
car_class_cty02 = tuple(zip(car_class, car_class_cty01))
car_class_cty02 = sorted(car_class_cty02, key=lambda data: data[1], reverse=True)
for data in car_class_cty02:
    print('자동차 특징 : {} 도시연비의 평균 : {}'.format(data[0], data[1]))
# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
hwy = []
hwy_count = []
with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[0] not in hwy:
            hwy.append(car_info[0])
            hwy_count.append([int(car_info[-3]), 1])
        else:
            hwy_count[-1][0] += int(car_info[-3])
            hwy_count[-1][1] += 1

hwy_avg01 = [data[0]/data[1] for data in hwy_count]
hwy_avg02 = tuple(zip(hwy, hwy_avg01))
hwy_avg02 = sorted(hwy_avg02, key=lambda data: data[1], reverse=True)
for i in range(3):
    print('제조사 : {} 고속도로 연비 평균 : {}'.format(hwy_avg02[i][0], hwy_avg02[i][1]))
# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
car_class = []
compact_car = []
with open('./word/mpg.txt', 'r') as file:
    file.readline()
    for car in file.readlines():
        car_info = car.strip('\n').split(',')
        if car_info[-1] == 'compact':
            if car_info[0] not in car_class:
                car_class.append(car_info[0])
                compact_car.append(1)
            else:
                compact_car[-1] += 1

compact_count = tuple(zip(car_class, compact_car))
compact_count = sorted(compact_count, key=lambda data: data[1], reverse=True)
print(compact_count)
for data in compact_count:
    print('제조사 : {} compact 차종 수 :{}'.format(data[0], data[1]))