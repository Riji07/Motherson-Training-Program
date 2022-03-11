class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
blue_car = Car(color="blue", mileage=20_000)
red_car = Car(color="red", mileage=30_000)
for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
        class GoldenRetriever(Dog):
            def speak(self, sound="Bark"):
                return super().speak(sound)