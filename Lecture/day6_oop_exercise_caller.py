from ai.oop.oop_exercise import *

# unit = Unit(10, 100)
# unit.unitInfo()

# 마린생성
marine1 = Marine(10, 100, 0, 0)
marine2 = Marine(10, 100, 0, 0)
marine3 = Marine(10, 100, 0, 0)
marine4 = Marine(10, 100, 0, 0)

# 메딕생성
medic1 = Medic(0, 100, 0)
medic2 = Medic(0, 100, 0)

# 병력을 리스트에 담음
trooplist = []
trooplist.append(marine1)
trooplist.append(marine2)
trooplist.append(marine3)
trooplist.append(marine4)
trooplist.append(medic1)
trooplist.append(medic2)

# 기본정보 출력
for instance in trooplist:
    instance.unitInfo()

# 드랍쉽생성
ship = Dropship(0, 50, 0)

# 부대원을 태움
ship.board(trooplist)

# 공격지점으로 이동
ship.attack()

# 부대원 내리기
troopattacklist = ship.drop()

# 공격
for unit in troopattacklist:
    if isinstance(unit, Marine):
        unit.stimpack()
    unit.attack()