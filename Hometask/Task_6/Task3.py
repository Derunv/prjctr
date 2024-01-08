def unique_elements(arr: list) -> list:
    # unique_list = [i for i in arr if arr.count(i) == 1]
    # for i in arr:
    #     if arr.count(i) == 1:
    #         unique_list.append(i)
    return [i for i in arr if arr.count(i) == 1]


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


test_unique_elements()
