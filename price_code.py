from enum import Enum
from datetime import datetime

from movie import Movie


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2 + 1.5 * (days - 2) if (days > 2) else 2,
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + 1.5 * (days - 3) if (days > 3) else 1.5,
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent(self, days: int) -> float:
        "Return the frequent points for a given number of days"""
        frequent = self.value["frp"]  # the enum member's frequent formula
        return frequent(days)

    @classmethod
    def for_movie(cls, movie: Movie):
        this_year = str(datetime.now().year)
        if movie.get_year == this_year:
            return cls.NEW_REALEASE
        elif movie.is_genre('Children'):
            return cls.CHILDREN
        else:
            return cls.REGULAR
