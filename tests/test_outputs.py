from fizzbuzzn.outputs import ConstOutput, ValueOutput


class Test_ConstOutput__Generate:
    def setup_method(self):
        self.output = ConstOutput('Fizz')

    def test_input_1(self):
        assert self.output.generate('1') == 'Fizz'

    def test_input_aaa(self):
        assert self.output.generate('aaa') == 'Fizz'


class Test_ValueOutput__Generate:
    def setup_method(self):
        self.output = ValueOutput()

    def test_input_1(self):
        assert self.output.generate('1') == '1'

    def test_input_aaa(self):
        assert self.output.generate('aaa') == 'aaa'
