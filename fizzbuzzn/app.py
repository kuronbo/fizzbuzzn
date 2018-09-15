def fizzbuzz(value: str) -> str:
    """FizzBuzzのルールのもと結果を返す

    Args:
        value: 数字
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | ``value``
    """
    num = int(value)

    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return value
