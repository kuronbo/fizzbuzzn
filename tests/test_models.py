from fizzbuzzn.evaluations import MultipleNumber


class TestMultipleNumber__IsValid:
    def setup_method(self):
        self.evaluation = MultipleNumber(5)

    def test_input_20_output_True(self):
        assert self.evaluation.is_valid('20') is True

    def test_input_m20_output_True(self):
        assert self.evaluation.is_valid('-20') is True

    def test_input_3_output_False(self):
        assert self.evaluation.is_valid('3') is False

    def test_input_m3_output_False(self):
        assert self.evaluation.is_valid('-3') is False
