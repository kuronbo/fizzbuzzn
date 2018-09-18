from fizzbuzzn import app


class Test_Fizzbuzz:
    def test_input_1_output_1(self):
        assert app.fizzbuzz(1) == '1'

    def test_input_45_output_FizzBuzz(self):
        assert app.fizzbuzz(45) == 'FizzBuzz'

    def test_input_10_output_Buzz(self):
        assert app.fizzbuzz(10) == 'Buzz'

    def test_input_99_output_Fizz(self):
        assert app.fizzbuzz(99) == 'Fizz'

    def test_input_0_output_0(self):
        assert app.fizzbuzz(0) == '0'
