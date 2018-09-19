from fizzbuzzn.utils import is_int


class Evaluation:
    def is_valid(self, value):
        raise NotImplementedError


class All(Evaluation):
    def is_valid(self, value):
        return True


class ConstNumber(Evaluation):
    def __init__(self, const):
        self.const = int(const)

    def is_valid(self, value):
        if is_int(value):
            return int(value) == self.const
        else:
            return False


class MultipleNumber(Evaluation):
    def __init__(self, multiple):
        self.multiple = int(multiple)

    def is_valid(self, value):
        if is_int(value):
            return int(value) % self.multiple == 0
        else:
            return False
