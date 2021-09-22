"""cp1404 practical of guitar class"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2021 - self.year

    def is_vintage(self):
        if 2021 - self.year > 50:
            return True
        else:
            return False


def run_tests():
    g1 = Guitar("Gibson L-5 CES", 1922, 16035)
    print(g1.get_age())
    print("Is vintage", g1.is_vintage())


if __name__ == '__main__':
    run_tests()
