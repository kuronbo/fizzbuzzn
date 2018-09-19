class Output:
    def generate(self, value):
        raise NotImplementedError


class ConstOutput(Output):
    def __init__(self, const):
        self.const = str(const)

    def generate(self, value):
        return self.const


class ValueOutput(Output):
    def generate(self, value):
        return value
