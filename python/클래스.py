# 클래스
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("hello! " + to_name + " i'm " +self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 나는 " + str(self.age) + " 살이야")

ruby = Person("ruby", 25)
dia = Person("dia", 26)
ruby.say_hello("bling")
dia.say_hello("bling")
ruby.introduce()
dia.introduce()

# 상속
class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다" + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("이걸 만들어야겠다! : " + to_program)

ruby =  Programmer("ruby", 25)
ruby.program("python")
dia = Police("dia", 26)
dia.arrest("thief")
