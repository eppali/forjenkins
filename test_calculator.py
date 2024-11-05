import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # Utilisation de assertEqual
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        # Utilisation de assertEqual
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertNotEqual(self.calc.subtract(10, 4), 5)  # Utilisation de assertNotEqual

    def test_multiply(self):
        # Utilisation de assertEqual
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertGreater(self.calc.multiply(5, 2), 8)  # Utilisation de assertGreater
        self.assertLess(self.calc.multiply(2, 3), 10)     # Utilisation de assertLess

    def test_divide(self):
        # Utilisation de assertEqual
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Utilisation de assertRaises pour vérifier l'exception
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        # Utilisation de assertAlmostEqual pour les valeurs flottantes
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=4)

    def test_is_instance(self):
        # Utilisation de assertIsInstance pour vérifier le type de l'objet
        self.assertIsInstance(self.calc, Calculator)

    def test_boolean(self):
        # Utilisation de assertTrue et assertFalse
        self.assertTrue(self.calc.add(0, 0) == 0)
        self.assertFalse(self.calc.multiply(1, 0) != 0)

if __name__ == '__main__':
    unittest.main()
