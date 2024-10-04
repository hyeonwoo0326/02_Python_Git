#1
def add(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

def multiply(num1, num2, num3, num4):
    result = num1 * num2 * num3 * num4
    return result

print(add(1, 2, 3, 4))
print(multiply(1, 2, 3, 4))

#2
def discriminator(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

print(discriminator(1))
print(discriminator(2))

#3
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(average([1, 2, 3, 4,5]))

#4
class GameCharacter:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character1 = GameCharacter("Player1", "남", "전사")
character1.attack()

#5
class Real_Estate:
    def __init__(self, location, size, type, price, built_year):
        self.location = location
        self.size = size
        self.type = type
        self.price = price
        self.built_year = built_year

    def show_info(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}")
        print(f"건물의 종류: {self.type}")
        print(f"가격: {self.price}")
        print(f"건물이 지어진 년도: {self.built_year}")

estate = Real_Estate("청주", 10, "아파트", 1000000, 2024)

estate.show_info()
