def fizzbuzz(num):
    """FizzBuzzのルールのもと結果を返す。

    `num`が3の倍数なら「Fizz」、5の倍数なら「Buzz」、3かつ5の倍数なら「FizzBuzz」、
    それ以外ならそのまま「`num`」を返す。
    また、この関数は0を倍数に含めないものとする（ex 0は5の倍数ではない。0の倍数は存在しない。）

    Args:
        num(int): 数字
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | str(`num`)
    """
    if num == 0:
        return str(num)

    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return str(num)
