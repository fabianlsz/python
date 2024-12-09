from functools import reduce


class Service:

    def filer_movies_by_actor(self, movies, actors):
        return list(filter(lambda m: actors, movies))

    def filter_movies_by_rating(self, movies, rating):
        return list(filter(lambda m: m.imdb_rating > rating, movies))

    def count_movies_by_actor(self, movies, actor):
        return sum(map(lambda m: actor in m.actors, movies))

    def average_rating_by_actor(self, movies, actor):
        relevant_movies = list(filter(lambda m: actor in m.actors, movies))
        total_rating = reduce(lambda acc, m: acc + m.imdb_rating, relevant_movies, 0)
        return total_rating / len(relevant_movies) if relevant_movies else 0
