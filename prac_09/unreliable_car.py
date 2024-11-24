import random
from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < random.randint(0, 100):
            distance = 0
        return super().drive(distance)