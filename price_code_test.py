import unittest

import self as self

from movie import Movie
from price_code import PriceCode


class RentalTest(unittest.TestCase):

    def test_rental_price(self):
        movie_type = PriceCode.new_release
        self.assertEqual(movie_type.price(days=3), 9)
        self.assertEqual(movie_type.price(days=5), 15.0)
        movie_type = PriceCode.normal
        self.assertEqual(movie_type.price(days=3), 3.5)
        self.assertEqual(movie_type.price(days=2), 2)
        movie_type = PriceCode.childrens
        self.assertEqual(movie_type.price(days=2), 1.5)
        self.assertEqual(movie_type.price(days=5), 4.5)

    def test_frequent_points(self):
        movie_type = PriceCode.new_release
        self.assertEqual(movie_type.frequent(5), 5)
        movie_type = PriceCode.normal
        self.assertEqual(movie_type.frequent(4), 1)
        movie_type = PriceCode.childrens
        self.assertEqual(movie_type.frequent(3), 1)
