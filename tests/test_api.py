from fizzbuzzn import app

class Test_Fizzbuzz__no_rule_list:
    def test_input_1_output_1(self):
        assert app.fizzbuzz("1") == "1"


class Test_Fizzbuzz__with_fizzbuzzgame_rule:
    def setup_method(self):
        self.rule_list = [
            (1, 15, 'FizzBuzz'),
            (2, 5, 'Buzz'),
            (2, 3, 'Fizz'),
        ]

    def test_input_1_output_1(self):
        assert app.fizzbuzz("-1", rule_list=self.rule_list) == "-1"

    def test_input_15_output_FizzBuzz(self):
        assert app.fizzbuzz("45", rule_list=self.rule_list) == "FizzBuzz"

    def test_input_5_output_Buzz(self):
        assert app.fizzbuzz("5", rule_list=self.rule_list) == "Buzz"

    def test_input_3_output_Fizz(self):
        assert app.fizzbuzz("3", rule_list=self.rule_list) == "Fizz"
