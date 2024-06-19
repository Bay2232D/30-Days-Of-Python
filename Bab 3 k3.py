class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

car = Car("Honda", "Civic", 2022)
print(car.get_make())
print(car.get_model())
print(car.get_year())
