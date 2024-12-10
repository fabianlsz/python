from datetime import datetime
from functools import reduce
from domain.validation import Validation
from repository.movie_repository import MovieRepository
from domain.movie_domain import Movie

class Service:
    def __init__(self, validator: Validation, repoMovie: MovieRepository):
        self.validator = validator
        self.MovieRepository = repoMovie

    def add_movie(self, title: str, release_date: datetime, imdb_rating: float, actors: list):
        for movie in self.MovieRepository.get_all():
            if movie.title == title:
                raise ValueError("Movie already exists!")
        idNewMovie = self.MovieRepository.gen_id_movies()
        newMovie = Movie(idNewMovie, title, release_date, imdb_rating, actors)
        self.validator.validator_movie(newMovie)
        self.MovieRepository.add(newMovie)

    def remove_movie(self, idMovie: int):
        self.MovieRepository.delete(idMovie)

    def update_movie(self, updated_movie: Movie):
        self.MovieRepository.update(updated_movie)

    def get_movie(self):
        return self.MovieRepository.get_all()

    def filter_movies_by_actor(self, movies: list, actor: str):
        return list(filter(lambda m: actor in m.actors, movies))

    def filter_movies_by_rating(self, movies: list, rating: float):
        return list(filter(lambda m: m.imdb_rating > rating, movies))

    def count_movies_by_actor(self, movies: list, actor: str):
        return sum(map(lambda m: actor in m.actors, movies))

    def average_rating_by_actor(self, movies: list, actor: str):
        relevant_movies = list(filter(lambda m: actor in m.actors, movies))
        total_rating = reduce(lambda acc, m: acc + m.imdb_rating, relevant_movies, 0)
        return total_rating / len(relevant_movies) if relevant_movies else 0
