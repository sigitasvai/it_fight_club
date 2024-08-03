class Car:
    def __init__(self, mark, model, top_speed):
        self.mark = mark
        self.model = model
        self.top_speed = top_speed

    def print_details(self):
        print(f"Mark: {self.mark}\nModel: {self.model}\nTop speed: {self.top_speed} km/h")


# my_car = Car("Fiat", "Punto", 145)
# my_car.print_details()

class ToyotaPrius(Car):
    def __init__(self):
        super().__init__("Toyota", "Prius", 165)
        self.top_speed_on_electricity = 30
        self.charge_status = 0

    def print_details(self):
        super().print_details()
        print(f"Top speed on electricity: {self.top_speed_on_electricity}")


my_toyota = ToyotaPrius()
my_toyota.print_details()
