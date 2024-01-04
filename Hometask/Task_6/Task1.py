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
