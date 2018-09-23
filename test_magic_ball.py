import unittest
from ball import blank_question, question, try_again, randomization


class TestMagic_ball(unittest.TestCase):

    def test_user_can_get_answer(self):
        """Test a user can get"""
        answer = randomization()
        self.assertTrue(randomization(), answer)

    def test_user_can_input_question(self):
        question_input = ""
        self.assertEqual(question(), question_input)

    def test_empty_input_raises_error(self):
        empty_input = "Please ask me a question"
        self.assertEqual(blank_question(), empty_input)

    def test_user_can_ask_another_question(self):
        question_two = "Would you like to ask the Wise One another question? Y/N:"
        self.assertEqual(try_again(), question_two)


if __name__ == '__main__':
    unittest.main()
