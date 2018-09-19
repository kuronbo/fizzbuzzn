from fizzbuzzn.outputs import ConstStr


class Test_ConstStr__Generate:
    def setup_method(self):
        self.output = ConstStr('Fizz')

    def test_input_1(self):
        assert self.output.generate('1') == 'Fizz'

    def test_input_aaa(self):
        assert self.output.generate('aaa') == 'Fizz'
