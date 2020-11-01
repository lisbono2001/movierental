import logging

from movie import Movie
from price_code import PriceCode


class Rental:
    """
	A rental of a movie by customer.
	From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
	rental period is calculated.
    But for simplicity of the example only a days_rented
	field is used.
    """

    def __init__(self, movie, days_rented):
        """
        Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_title(self):
        return self.movie.gettitle()

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_frequent_rental_point(self):
        price_code = PriceCode.for_movie(self.movie)
        return price_code.frequent_rental_points(self.days_rented)

    def get_charge(self):
        price_code = PriceCode.for_movie(self.movie)
        return price_code.price(self.days_rented)
