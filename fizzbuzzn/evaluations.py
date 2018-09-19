from fizzbuzzn.utils import is_int


class Evaluation:
    def is_valid(self, value):
        raise NotImplementedError


class MultipleNumber(Evaluation):
    def __init__(self, multiple):
        self.multiple = int(multiple)

    def is_valid(self, value):
        if is_int(value):
            return int(value) % self.multiple == 0
        else:
            return False
