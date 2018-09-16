from collections import Sequence


def fizzbuzz(value: str, rule_list: Sequence=None) -> str:
    """クライアント定義のルールのもと結果を返す

    ``value``でルールリストを走査し、``value``が倍数条件に合えば
    設定されている出力を返す。また、全てのルールに合わない``value``は、
    そのまま``value``を返す。
    ``rule_list``はtuple(priority<int>, mulitple<int>, output<str>)
    のリスト。
    Args:
        value: 数字
        rule_list: ルールリスト。ルール➡(優先順位, 倍数, 出力)
    Return:
        'FizzBuzz' | 'Buzz' | 'Fizz' | ``value``
    """
    num = int(value)
    if rule_list:
        rules = [(int(mul), str(out)) for _, mul, out in sorted(rule_list)]
    else:
        rules = []

    for mul, out in rules:
        if num % mul == 0:
            return out
    return value


if __name__ == '__main__':
    rule_list = [
        (1, 15, 'FizzBuzz'),
        (2, 5, 'Buzz'),
        (2, 3, 'Fizz'),
    ]
    print(fizzbuzz("15", rule_list))
