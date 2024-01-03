def int_to_roman(s: int) -> str:
    roman_symbol_value = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }
    result = ""

    for value, numeral in roman_symbol_value.items():
        while s >= value:
            result += numeral
            s -= value
    return result


def test_int_to_roman():
    result1 = int_to_roman(3)
    assert result1 == "III"

    result1 = int_to_roman(58)
    assert result1 == "LVIII"

    result1 = int_to_roman(1994)
    assert result1 == "MCMXCIV"


# print(int_to_roman(58))
test_int_to_roman()
