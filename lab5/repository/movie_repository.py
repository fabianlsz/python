from domain.movie_domain import Movie

class MovieRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__movies = []
        self.__load()

    def __save(self, movies):
        with open(self.file_path, "w") as file:
            for movie in movies:
                actors = ";".join(movie.actors)
                file.write(f"{movie.movie_id},{movie.title},{movie.release_date.strftime('%d-%m-%Y')},{movie.imdb_rating},{actors}\n")

    def __load(self):
        movies = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    movie_id, title, release_date, imdb_rating, actors = line.strip().split(",")
                    movies.append(Movie(int(movie_id), title, release_date, float(imdb_rating), actors.split(";")))
        except FileNotFoundError:
            pass
        return movies

    def get_all(self) -> list:
        return self.__movies

    def gen_id_movies(self):
        return max([e.user_id for e in self.__movies], default=0) + 1


    def find(self, movie_id):
        for index, user in enumerate(self.__movies):
            if user.get_user_id() == movie_id:
                return index
        return -1


    def add(self, movie: Movie):
        if self.find(movie.get_movie_id()) != -1:
            raise ValueError("The movie already exists!")
        self.__movies.append(movie)

    def update(self, movieupdated: Movie):
        pos = self.find(movieupdated.get_movie_id())
        if pos == -1:
            raise ValueError("The movie with the given id doesn't exist!")
        self.__movies[pos] = movieupdated

    def delete(self, idMovie: int):
        pos = self.find(idMovie)
        if pos == -1:
            raise ValueError("The movie with the given id doesn't exist!")
        del self.__movies[pos]

