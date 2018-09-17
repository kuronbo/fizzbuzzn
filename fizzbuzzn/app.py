def fizzbuzz(num, zeroable=True):
    """FizzBuzzのルールのもと結果を返す

    Args:
        num(int): 数字
    Kwargs:
        zeroable(bool): 0を全ての倍数として扱うかどうか
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | str(`num`)
    """
    if not zeroable:
        return '0'

    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return str(num)
