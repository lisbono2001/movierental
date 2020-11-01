# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.
from _csv import reader

from movie import Movie
from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog

# def make_movies():
#     movies = [
#         Movie("The Irishman", Movie.NEW_RELEASE),
#         Movie("CitizenFour", Movie.REGULAR),
#         Movie("Frozen", Movie.CHILDRENS),
#         Movie("El Camino", Movie.NEW_RELEASE),
#         Movie("Particle Fever", Movie.REGULAR)
#     ]
#     return movies

if __name__ == '__main__':
    mc = MovieCatalog()
    print(mc.get_movie("The Arrival"))
    # # Create a customer with some rentals
    # movies = MovieCatalog().get_movie
    # 
    # customer = Customer("Edward Snowden")
    # days = 1
    # for movie in movies:
    #     customer.add_rental(Rental(movie, days))
    #     days += 1
    # print(customer.statement())
