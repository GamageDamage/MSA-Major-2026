import datetime


class Automoblie():
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year
        self.color = color


    def print_data(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine Size: {self.engine_size}")
        print(f"Owner: {self.owner}, Color: {self.color}\n")
        pass

    def get_age(self):
        the_date = datetime.datetime.now()
        this_year = the_date.year

        return this_year-self.year