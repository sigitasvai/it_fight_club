class EcoSystem:
    def __init__(self):
        pass

    def add(self):
        pass


class EcoSystemItem:
    def __init__(self, name):
        self.name = name

    def simulate_day(self):
        return {
            "co2_m3": self.affect_co2_m3(24),
            "oxygen_m3": self.affect_oxygen_m3(24)
        }

    def affect_co2_m3(self, hours):
        pass

    def affect_oxygen_m3(self, hours):
        pass


class Tree(EcoSystemItem):
    def __init__(self):
        super().__init__("Uosis")


my_ecosystem = EcoSystem()
my_ecosystem.add(Tree())
