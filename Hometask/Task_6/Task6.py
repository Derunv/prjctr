cities_population = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
    ]


def city_population(city: tuple) -> int:
    # Return city population
    return city[1]


def city_population_sort(city: list) -> list:
    # Sort list and calculate statistic data (average_population, total_population)
    city.sort(reverse=True, key=city_population)
    total_population = 0
    for i in city:
        total_population += i[1]
    average_population = total_population / len(city)
    return [average_population, total_population]


statistic_data = city_population_sort(cities_population)
print(f' Total population {statistic_data[1]} and average population {statistic_data[0]}')
