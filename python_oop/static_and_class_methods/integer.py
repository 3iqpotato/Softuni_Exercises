class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))


    @classmethod
    def from_roman(cls, value):
            value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            n = 0
            last_digit_value = 0

            for roman_digit in value[::-1]:  # 1
                digit_value = value_map[roman_digit]

                if digit_value >= last_digit_value:  # 2
                    n += digit_value
                    last_digit_value = digit_value
                else:  # 3
                    n -= digit_value

            return cls(n)

    @classmethod
    def from_string(cls, value):
        try:
            if value.isdigit():
                n = int(value)
        except AttributeError:
            return "wrong type"

        return cls(n)

first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
