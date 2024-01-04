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
