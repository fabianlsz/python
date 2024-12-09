from datetime import datetime


class Movie:
    def __init__(self, movie_id, title, release_date, imdb_rating, actors):
        self.movie_id = movie_id
        self.title = title
        self.release_date = datetime.strptime(release_date, "%d-%m-%Y")
        self.imdb_rating = imdb_rating
        self.actors = actors

    def get_actors(self):
        return self.actors

    def set_actors(self, value):
        self.actors = value

    def get_release_date(self):
        return self.release_date

    def set_release_date(self, value):
        self.release_date = value

    def get_movie_id(self):
        return self.movie_id

    def set_movie_id(self, value):
        self.movie_id = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_imdb_rating(self):
        return self.imdb_rating

    def set_imdb_rating(self, value):
        self.imdb_rating = value

    def __str__(self):
        release_date_str = self.release_date.strftime("%d-%m-%Y")
        return f"Movie[ID={self.movie_id}, Title={self.title}, Release Date={release_date_str}, IMDb Rating={self.imdb_rating}, Actors={self.actors}]"
