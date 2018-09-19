class Output:
    def generate(self, value):
        raise NotImplementedError


class ConstStr(Output):
    def __init__(self, const):
        self.const = str(const)

    def generate(self, value):
        return self.const
