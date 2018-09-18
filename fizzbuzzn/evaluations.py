class Evaluation:
    def is_valid(self, value):
        raise NotImplementedError


class MultipleNumber(Evaluation):
    def __init__(self, multiple):
        self.multiple = int(multiple)

    def is_valid(self, value):
        num = int(value)
        return num % self.multiple == 0
