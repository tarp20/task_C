import unittest

import car


class TestCar(unittest.TestCase):
    def test_is_car_exist(self):
        self.assertTrue(car.is_car_exist('honda', 'civic'))
        self.assertFalse(car.is_car_exist('Curana', 'merana'))
        self.assertTrue(car.is_car_exist('BMW', 'X5'))
        self.assertFalse(car.is_car_exist('BMW', 'X29'))
