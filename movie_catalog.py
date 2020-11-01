from csv import reader
from movie import Movie


class MovieCatalog:
    MOVIES_FILE = "movies.csv"

    def __init__(self):
        self.moviecatalog = self.load_movie(self.MOVIES_FILE)

    def load_movie(self, file):
        movies = []
        with open(file, 'r') as read_obj:
            csv_reader = reader(read_obj)
            for movie in list(csv_reader):
                movies.append(Movie(movie[1], movie[2], movie[3].split("|"), movie[0]))
        return movies

    def get_movie(self, title):
        for movie in self.moviecatalog:
            if movie.get_title() == title:
                return movie
        raise KeyError("Error! Movie not found.")


if __name__ == '__main__':
    mc = MovieCatalog()
    print(mc.get_movie("Mulan"))
