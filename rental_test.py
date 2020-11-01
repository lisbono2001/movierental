import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Mulan", 2020, ['Action'])
		self.regular_movie = Movie("The Martian",2015, ['Adventure'])
		self.childrens_movie = Movie("The Legend of Sarila",2013, ['Children'])

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_charge(), 15.0)

		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_charge(), 3.5)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_charge(), 2)

		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.get_charge(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_charge(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_frequent_rental_point(), 5)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_frequent_rental_point(), 1)
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_frequent_rental_point(), 1)
