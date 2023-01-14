class Country():
    population = 0

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population


class Russia(Country):
    {}


class Canada(Country):
    {}


class Germany(Country):
    {}


rus = Russia()
rus.setPopulation(50)
print(rus.getPopulation())

can = Canada()
can.setPopulation(100)
print(can.getPopulation())

gem = Germany()
gem.setPopulation(150)
print(gem.getPopulation())
