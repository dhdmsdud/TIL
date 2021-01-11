from ai.oop.oop_inheritance import *
# Car1 = Car("Gv70", 4, 2400)
# Car1.carinfo()

# parent = Parent("부모", "공무원")
# print(parent.display())

# child01 = Child01("자식", "강사", 49)
# child01.childinfo()

# stu01 = StudentVO("은영", 25, "anyang", "2017")
# print(stu01.stuinfo())

# teacher01 = TeacherVO("섭섭", 49, "seoul", "python")
# print(teacher01.teachinfo())

# emp01 = ManagerVO("장호연", 29, "seoul", "hrd")
# print(emp01.emptinfo())

# userDate = Mydate()
# userDate.setYear()
# print(userDate.getYear())

# hiding = HidingClass("홍길동", "교육팀", 100)
# print(hiding.name)
# print(hiding.dept)
# print(hiding.num)
# print(hiding.utype)
# print(hiding.getDept())
# print(hiding.__getDept())

# 다형성
# stu01 = StudentVO("은영", 25, "anyang", "2017")
# teacher01 = TeacherVO("섭섭", 49, "seoul", "python")
# emp01 = ManagerVO("장호연", 29, "seoul", "hrd")
#
# perlist = []
# perlist.append(stu01)
# perlist.append(teacher01)
# perlist.append(emp01)

# for obj in perlist: #version1
#     if isinstance(obj, StudentVO):
#         print(obj.stuinfo())
#     elif isinstance(obj, TeacherVO):
#         print(obj.teachinfo())
#     else :
#         print(obj.emptinfo())

# for obj in perlist: #version2
#     print(obj.perinfo())

# account = Account("441-2919-1234", 500000, 0.073)
# account.accountInfo()
# account.withDraw(600000)
# account.deposit(200000)
# account.accountinfo()
# account.withDraw(600000)
# account.accountinfo()
# print("현재 잔액의 이자를 포함한 금액")
# account.printInterestRate()

account = FundAccount("441-2919-1234", 500000, 0.073, "F")
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountinfo()
account.withDraw(600000)
account.accountinfo()
print("현재 잔액의 이자를 포함한 금액")
account.printInterestRate()
