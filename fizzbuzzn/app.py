from fizzbuzzn.evaluations import MultipleNumber, ConstNumber, All
from fizzbuzzn.outputs import ConstOutput, ValueOutput


def fizzbuzz(value):
    """FizzBuzzのルールのもと結果を返す。

    `num`が3の倍数なら「Fizz」、5の倍数なら「Buzz」、3かつ5の倍数なら「FizzBuzz」、
    それ以外ならそのまま「`value`」を返す。
    また、この関数は0を倍数に含めないものとする（ex 0は5の倍数ではない。0の倍数は存在しない。）

    Args:
        value(str): 変換前の値
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | `value`
    """
    rules = [
        (ConstNumber(0), ValueOutput()),
        (MultipleNumber(15), ConstOutput('FizzBuzz')),
        (MultipleNumber(5), ConstOutput('Buzz')),
        (MultipleNumber(3), ConstOutput('Fizz')),
        (All(), ValueOutput())
    ]
    for ev, output in rules:
        if ev.is_valid(value):
            return output.generate(value)
