def fizzbuzz(num):
    """FizzBuzzのルールのもと結果を返す

    Args:
        num(int): 数字
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | str(`num`)
    """
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return str(num)
