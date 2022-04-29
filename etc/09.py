# # 예제 9

# 클래스 상속
class Car:
    name = ""
    speed = 0

    def upSpeed(self, val):
        self.speed += val

    def downSpeed(self, val):
        self.speed -= val

    def getSpeed(self):
        print("스피드 출력 : 오버라이딩")


class Sedan(Car):
    seanNum = 0

    def getSpeed(self):
        return self.speed


class Sport(Car):
    capacity = 0

    def getSpeed(self):
        return self.speed


sedan1 = Sedan()
sport1 = Sport()

sedan1.upSpeed(50)
print(sedan1.speed)

sedan1 = Car()



