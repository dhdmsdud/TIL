class Car(object):
    def __init__(self, car_data):
        car_data = car_data.split(",")
        self.manufacturer = car_data[0]
        self.model = car_data[1]
        self.displ = float(car_data[2])
        self.year = int(car_data[3])
        self.cyl = int(car_data[4])
        self.trans = car_data[5]
        self.drv = car_data[6]
        self.cty = int(car_data[7])
        self.hwy = int(car_data[8])
        self.fl = car_data[9]
        self.car_class = car_data[10]

    def __repr__(self):
        return self.manufacturer + ", " + self.model \
               + "," + self.displ + ", " + self.year \
               + self.trans + ", " + self.drv \
               + self.cty + ", " + self.hwy \
               + self.cyl + ", " + self.fl + ", " + self.car_class

with open(file="./word/mpg.txt", mode="r", encoding="utf8")as file:
    car_list = list()
    line = file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        car_list.append(Car(line.strip()))

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
#    어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
displ04 = []
displ05 = []

for obj in car_list:
    if obj.displ <=4:
        displ04.append(obj.hwy)
    elif obj.displ >= 5:
        displ05.append(obj.hwy)

avg04 = sum(displ04) / len(displ04)
print("배기량이 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg04))
avg05 = sum(displ05) / len(displ05)
print("배기량이 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg05))

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# # "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# # 평균적으로 더 높은지 확인하세요.
audi_cty = []
toyota_cty = []

for obj in car_list:
    if obj.manufacturer == "audi":
        audi_cty.append(obj.cty)
    elif obj.manufacturer == "toyota":
        toyota_cty.append(obj.cty)

avg_audi_cty = sum(audi_cty) / len(audi_cty)
print("audi 도시연비의 평균 : {}".format(avg_audi_cty))
avg_toyota_cty = sum(toyota_cty) / len(toyota_cty)
print("toyota 도시연비의 평균 : {}".format(avg_toyota_cty))

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
chevrolet_hwy = []
ford_hwy = []
honda_hwy = []

for obj in car_list:
    if obj.manufacturer == "chevrolet":
        chevrolet_hwy.append(obj.hwy)
    elif obj.manufacturer == "ford":
        ford_hwy.append(obj.hwy)
    elif obj.manufacturer == "honda":
        honda_hwy.append(obj.hwy)

avg_chevrorlet_hwy = sum(chevrolet_hwy) / len(chevrolet_hwy)
print("chevrorlet의 고속도로 평균 연비 : {}".format(avg_chevrorlet_hwy))
avg_ford_hwy = sum(ford_hwy) / len(ford_hwy)
print("ford의 고속도로 평균 연비 : {}".format(avg_chevrorlet_hwy))
avg_honda_hwy = sum(honda_hwy) / len(honda_hwy)
print("honda의 고속도로 평균 연비 : {}".format(avg_honda_hwy))

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요. sort사용
audi_hwy = []
for obj in car_list:
    if obj.manufacturer == "audi":
        audi_hwy.append(obj.hwy)

audi_hwy.sort(reverse=True)
print(audi_hwy[:5])

# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.
suv_list = []
for obj in car_list:
    avg_data = (obj.hwy + obj.cty) / 2
    if obj.car_class == "suv":
        suv_list.append(obj)
data = reversed(sorted(suv_list, key=lambda object : object.avg_data))
print(suv_list)

cnt = 0
for i in range(len(suv_list)):
    cnt += 1
    print("회사 : {} , 평균연비 : {} ".format(suv_list[i].manufacturer,suv_list[i].avg_data))
    if cnt == 5:
        break

# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# # 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# # class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.
mpg_data = [obj.car_class for obj in car_list]
mpg_set = set(mpg_data)

def car(car_class):
    car_feature = [obj.cty for obj in car_list if obj.car_class == car_class]
    cty_avg = sum(car_feature) / len(car_feature)
    return (car_class, cty_avg)

result = []
for obj in mpg_set:
    result.append(car(obj))
data = reversed(sorted(result, key=lambda t : t[1]))
for i in data:
    print("class : {} , cty평균 : {}".format(i[0],i[1]))
# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
