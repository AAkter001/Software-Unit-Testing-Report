import unittest
from guess_the_number import generate_secret_number, evaluate_guess

class TestGuessTheNumber(unittest.TestCase):

    def test_generate_secret_number(self):
        
        secret_number = generate_secret_number()
        self.assertIsInstance(secret_number, int)
        self.assertTrue(1000 <= secret_number <= 9999)

    def test_evaluate_guess(self):
        secret_number = 1234

        # Correct guess
        result = evaluate_guess(secret_number, 1234)
        self.assertEqual(result, "Correct!")

        # All digits correct but in the wrong order
        result = evaluate_guess(secret_number, 4321)
        self.assertEqual(result, "4 x")

        # One digit correct and in the right spot
        result = evaluate_guess(secret_number, 1245)
        self.assertEqual(result, "1 circle")

        # One digit correct but in the wrong spot
        result = evaluate_guess(secret_number, 3412)
        self.assertEqual(result, "1 x")

        # No digit correct
        result = evaluate_guess(secret_number, 5678)
        self.assertEqual(result, "0")

if __name__ == '__main__':
    unittest.main()
    