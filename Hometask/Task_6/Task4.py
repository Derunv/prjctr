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
