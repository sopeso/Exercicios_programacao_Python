def fizz_buzz (num_inteiro):
    if num_inteiro % 3 == 0:
        return 'Fizz'
    elif num_inteiro % 5 == 0:
        return 'Buzz'
    elif num_inteiro % 5 == 0 and num_inteiro % 3 ==0 :
        return 'FizzBuzz'
    else:
        return num_inteiro
    