def two_sum():
    num1, num2 = 5, 7
    result = num1 + num2
    print(result)


def reverse_string():
    s = "hello"
    reversed_s = s[::-1]
    print(reversed_s)


def string_length():
    s = "hello"
    length = len(s)
    print(length)


def concatenate_string():
    s1 = "hello"
    s2 = "world"
    concatenated = s1 + s2
    print(concatenated)


def is_vowel():
    char = "a"
    result = char.lower() in "aeiou"
    print(result)


def swap_first_last():
    s = "hello"
    swapped = s[-1] + s[1:-1] + s[0]
    
    print(swapped)


def to_uppercase():
    s = "hello"
    upper_s = s.upper()
    print(upper_s)


def rectangle_area():
    length = 5
    width = 3
    area = length * width
    print(area)


def is_even():
    num = 4
    result = num % 2 == 0
    print(result)


def extract_first_three():
    s = "hello"
    first_three = s[:3]
    print(first_three)


def string_interpolation():
    name = "Alice"
    age = 30
    message = f"My name is {name} and I am {age} years old."
    print(message)


def string_slicing():
    s = "helloworld"
    sliced = s[2:6]
    print(sliced)


def type_conversion():
    num_str = "123"
    num = int(num_str)
    print(num)


def string_repetition():
    s = "hello"
    repeated = s * 3
    print(repeated)


def calculate_quotient_remainder():
    num1, num2 = 10, 3
    quotient = num1 // num2
    remainder = num1 % num2
    print(f"Quotient: {quotient}, Remainder: {remainder}")


def float_division():
    num1, num2 = 5, 2
    result = num1 / num2
    print(result)


def string_methods():
    s = "hello"
    count = s.count("l")
    print(count)


def escape_sequences():
    s = "She said, \"Hello!\""
    print(s)


def multi_line_string():
    s = """This is a
    multi-line
    string"""
    print(s)


def exponentiation():
    base = 2
    exponent = 3
    result = base**exponent
    print(result)


def exponentiation2():
    s = "racecar"
    result = s == s[::-1]
    print(result)


def check_anagrams():
    s1 = "listen"
    s2 = "silent"
    result = sorted(s1.lower()) == sorted(s2.lower())
    print(result)

if __name__ == "__main__":
    two_sum()
    reverse_string()
    string_length()
    concatenate_string()
    is_vowel()
    swap_first_last()
    to_uppercase()
    rectangle_area()
    is_even()
    extract_first_three()
    string_interpolation()
    string_slicing()
    type_conversion()
    string_repetition()
    calculate_quotient_remainder()
    float_division()
    string_methods()
    escape_sequences()
    multi_line_string()
    exponentiation()
    exponentiation2()
    check_anagrams()