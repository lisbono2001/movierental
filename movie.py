import logging

# from price_code import PriceCode

class Movie:
    """
	A movie available for rent.
	"""
    # REGULAR = PriceCode.normal
    # NEW_RELEASE = PriceCode.new_release
    # CHILDRENS = PriceCode.childrens

    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, year, genres):
        # Initialize a new movie. 
        self.__title = title
        self.__year = year
        self.__genres = genres

    @property
    def get_year(self):
        # property decorator for year getter
        return self.__year

    @property
    def get_title(self):
        # property decorator for title getter
        return self.__title

    def is_genre(self, genre):
        # check if specific genre in this movie genres
        return genre in self.__genres

    # def get_price_code(self):
    # 	# get the price code
    # 	return self.price_code
    # 
    # def get_title(self):
    # 	return self.title
    # 
    # def get_genres(self):
    # 	return self.genres
    # 
    # def get_charge(self, days_rented):
    # 	return self.price_code.price(days_rented)
    # 
    # def get_frequent(self, days_rented):
    # 	return self.price_code.frequent(days_rented)

    def __str__(self):
        return self.__title
