class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        # self.mileage = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed > 5:
            self.speed -= 5
        else:
            self.speed = 0
            print(f'Car can`t drive slower. The speed {self.speed} ')

    def display_speed(self):
        return self.speed

car1 = Car('Mercedes', 'S500', 2018, 50)
car1.accelerate()
car1.brake()
print(car1.speed)

