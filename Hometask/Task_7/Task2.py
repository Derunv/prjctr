def roman_to_int(s: str) -> int:
    roman_symbol_value = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000 }
    converted_value = []
    for i in range(len(s)):
        converted_value.append(roman_symbol_value[s[i]])
        if i != 0:
            if converted_value[i - 1] < converted_value[i]:
                converted_value[i - 1] = - converted_value[i - 1]
    return sum(converted_value)

def test_roman_to_int():
     result1 = roman_to_int("III")
     assert result1 == 3
     result1 = roman_to_int("LVIII")
     assert result1 == 58
     result1 = roman_to_int("MCMXCIV")
     assert result1 == 1994

test_roman_to_int()