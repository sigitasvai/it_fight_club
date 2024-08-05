class EcoSystem:
    def __init__(self):
        self.total_ecosystem_items = []
        self.total_oxygen = 0
        self.total_co2 = 0
        self.days = 0

    def add(self, name):
        self.total_ecosystem_items.append(name)

    def run(self, days):
        for eco_item in self.total_ecosystem_items:
            self.total_oxygen = + eco_item.calculation["oxygen_m3"]
            self.total_co2 = + eco_item.calculation["co2_m3"]

        self.total_oxygen *= days
        self.total_co2 *= days
        self.days = days

    def print_state(self):
        print(f"Day Passed: {self.days} ")
        print(f"Oxygen Available: {self.total_oxygen}")
        print(f"CO2 Available: {self.total_co2} ")
        print(f"Conclusion: ")


class EcoSystemItem:
    def __init__(self, name):
        self.name = name

    def simulate_day(self):
        return {
            "co2_m3": self.affect_co2_m3(24),
            "oxygen_m3": self.affect_oxygen_m3(24)
        }

    def affect_co2_m3(self, hours):
        if self.co2_consumes_m3_per_hour:
            return -(self.co2_consumes_m3_per_hour * hours)

    def affect_oxygen_m3(self, hours):
        if self.oxygen_produces_m3_per_hour:
            return self.oxygen_produces_m3_per_hour * hours
        elif self.oxygen_consumes_m3_per_hour:
            return -(self.oxygen_consumes_m3_per_hour * hours)


class Tree(EcoSystemItem):
    def __init__(self):
        super().__init__("Uosis")
        self.oxygen_produces_m3_per_hour = 0.1
        self.co2_consumes_m3_per_hour = 11.1
        self.calculation = super().simulate_day()


class Cow(EcoSystemItem):
    def __init__(self):
        super().__init__("Zalmarge")
        self.oxygen_produces_m3_per_hour = 0
        self.oxygen_consumes_m3_per_hour = 10
        self.co2_consumes_m3_per_hour = 0.5
        self.calculation = super().simulate_day()


my_ecosystem = EcoSystem()
my_ecosystem.add(Tree())
my_ecosystem.add(Tree())
my_ecosystem.add(Cow())
my_ecosystem.run(days=15)
my_ecosystem.print_state()
