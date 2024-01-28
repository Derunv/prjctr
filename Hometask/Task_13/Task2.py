class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        return Country(self.name + ' ' + other.name, self.population + other.population)

    def __str__(self):
        return f'Country: {self.name} with population {self.population}'
    # def add(self, other):
    #     return Country(other.name)
    #     # return Country(self.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina

# bosnia_herzegovina = bosnia.add(herzegovina)
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

print(bosnia_herzegovina.name)