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
