def majority_element(nums: list) -> int:
    nums_lib = {}
    for num in nums:
        if num in nums_lib:
            nums_lib[num] += 1
        else:
            nums_lib[num] = 1
    max_value = 0
    key = None
    for num, value in nums_lib.items():
        if value > max_value:
            max_value = value
            key = num
    #max_num = (max(nums_lib.values()), nums_lib.keys())
    return key


def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result1 == 2

test_majority_element()