class Unit(object):
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life

    def unitInfo(self):
        print("타입{}".format(self.utype))
        print("공격력{}".format(self.damage))
        print("생명력{}".format(self.life))

    def attack(self):
        pass

# 마린
class Marine(Unit):
    def __init__(self, damage, life, offense, defense):
        super().__init__(damage, life)
        self.offense = offense
        self.defense = defense

    def unitInfo(self):
        super().unitInfo()
        print("공격력 업그레이드 {}".format(self.offense))
        print("방어력 업그레이드 {}".format(self.defense))

    def attack(self):
            print("마린이 공격합니다.")

    def stimpack(self):
        if self.life > 50 :
            self.damage *= 1.5
            self.life -= 10
            print("마린이 스팀팩을 사용합니다.")
        else:
            print("체력이 낮아 사용불가합니다.")

# 메딕
class Medic(Unit):
    def __init__(self, damage, life, defense):
        super().__init__(damage, life)
        self.defense = defense

    def unitInfo(self):
        super().unitInfo()
        print("방어력 업그레이드 {}".format(self.defense))

    def attack(self):
        print("메딕이 마린을 치료합니다.")

# 드랍쉽
class Dropship(Unit):
    def __init__(self, damage, life, defense):
        super().__init__(damage, life)
        self.defense = defense

    def unitInfo(self):
            super().unitInfo()
            print("방어력 업그레이드 {}".format(self.defense))

    def attack(self):
        print("목표지점으로 이동합니다.")

    def board(self, unitType):
        self.unitType = unitType
        print("부대원을 태웠습니다.")

    def drop(self):
        print("모든 부대원이 내립니다.")
        return self.unitType