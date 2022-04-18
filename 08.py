# # 예제 8

# 클래스 기본
class Car:
    name = ""
    color = "red"
    speed = 0
    count = 0

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def setSpeed(self, spd):
        self.speed = spd

    def getSpeed(self):
        return self.speed

    def upSpeed(self, val):
        self.speed += val

    def downSpeed(self, val):
        self.speed -= val


a = Car("Audi", "White", 30)
print("이름:", a.name, "색상:", a.color, "속도:", a.speed)

b = Car("Benz", "Black", 50)
print("이름:", b.name, "색상:", b.color, "속도:", b.speed)

# 스태틱 변수
a.count += 1
print(a.count)

Car.count += 1
b.count += 1
print(b.count)
