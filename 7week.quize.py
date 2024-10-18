#1
import random

def lotto():
    result = []
    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result:
            result.append(num)
    return result

print(lotto())


#2
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f'{self.num} * {i} = {self.num * i}')

gugudan_3 = Gugudan(3)
gugudan_3.output()


#3
class Car:
    def __init__(self, model, color, mileage):
        self.model = model #모델명
        self.color = color #색상
        self.mileage = mileage #주행 거리

    def drive(self, distance): #주행 거리를 증가시키는 함수
        if distance > 0:
            self.mileage += distance
            print(f"{distance}km 주행했습니다. 현재 주행 거리는 {self.mileage}km입니다.")
        else:
            print("주행 거리는 0 이상이어야 합니다.")

    def paint(self, new_color): #자동차의 색상을 변경하는 함수
        old_color = self.color
        self.color = new_color
        print(f"자동차 색상이 {old_color}에서 {new_color}로 변경되었습니다.")

    def get_info(self): #자동차의 정보를 출력하는 함수
        return f"모델: {self.model}, 색상: {self.color}, 주행 거리: {self.mileage}km"


#예시 실행
my_car = Car("SANTA FE", "Gray", 19000)

#자동차 정보 출력
print(my_car.get_info())

#주행 60km
my_car.drive(60)

#색상 변경
my_car.paint("White")

#업데이트 된 자동차 정보 출력
print(my_car.get_info())

