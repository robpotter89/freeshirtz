from unittest import TestCase
from main import brute_force_shirt, ml_shirt_acquiry, SHIRT_MESSAGE, NUM_SHIRTS


class TestShirtAcquiry(TestCase):
    def test_ml_shirt_acquiry(self):
        result = ml_shirt_acquiry()
        self.assertEqual(result, SHIRT_MESSAGE)

    def test_brute_force_shirt_acquiry(self):
        result = brute_force_shirt()
        self.assertEqual(len(result), NUM_SHIRTS)
        for r in result:
            self.assertEqual(r, SHIRT_MESSAGE)
