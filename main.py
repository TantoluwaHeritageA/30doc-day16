def int_to_roman(num):
    result = ''
    roman_chart = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                   90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    while num != 0:
        for key, val in roman_chart.items():
            if num >= key:
                # print(key)
                quotient = int(num // key)
                num = num % key
                # print(num)
                result += quotient * val
    return result


num = int(input("Enter a number: "))
print(f"The roman numeral is  {int_to_roman(num)}")
