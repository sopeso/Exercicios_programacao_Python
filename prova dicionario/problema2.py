def transform_number_to_roman_numeral(number):
    roman_value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    for i in range(len(roman_value_list)):
        while number >= roman_value_list[i]:
            number -= roman_value_list[i]
            res += roman_char_list[i]
    return res
 
 
number_input = int(input("Digite um número:"))
roman_numeral_output = transform_number_to_roman_numeral(number_input)
print("Número Romano:",roman_numeral_output)
