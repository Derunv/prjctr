# Task 1
def compute_difference(first: list, second: list) -> tuple:
    #
    first_second = first[:]
    second_first = second[:]
    for i in range(len(first)):
        if first[i] in second_first:
            second_first.remove(first[i])
            first_second.remove(first[i])
    return first_second, second_first
    pass


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


test_compute_difference()


# Task 2
def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
        if target - nums[i] in nums[(nums.index(nums[i]))+1:]:
            result_list = [nums.index(nums[i]), nums[i + 1:].index(target-nums[i]) + i + 1]
            # Cut list to avoid use the same index number
            return result_list


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([1, 1, 3, 3, 3], 6)
    assert result3 == [2, 3]


test_sum_of_two()

# Task 3

def unique_elements(arr: list) -> list:
    unique_list = [i for i in arr if arr.count(i) == 1]
    # for i in arr:
    #     if arr.count(i) == 1:
    #         unique_list.append(i)
    return unique_list


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


test_unique_elements()


# Task 4

def odd_elements(arr: list) -> list:
    unique_list = []
    # unique_list = [i for i in arr if i not in unique_list and arr.count(i) % 2== 1] Not working
    for i in arr:
        if i not in unique_list and arr.count(i) % 2 == 1:
            unique_list.append(i)
    return unique_list


def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result1 == [1, 3, 4, 6]


test_odd_elements()


# Task 5

def second_largest_element(arr: list) -> int:
    if sum(arr) / arr[0] == len(arr):
        return None
    del arr[arr.index(max(arr))]
    return max(arr)


def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None


test_second_largest_element()


# Task 6

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
