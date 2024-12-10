from domain.movie_domain import Movie
from domain.user_domain import User


class Validation:
    def validator_user(self, user: User):
        erori = ""
        if user.name == "":
            erori += "Name is invalid! "
        if user.age == "":
            erori += "Age is invalid! "
        if len(erori) > 0:
            raise ValueError(erori)

    def validator_movie(self, movie: Movie):
        erori = ""
        if movie.title == "":
            erori += "Titlu invalid!"
        if movie.actors == "":
            erori += "Actori invalizi!"
        if movie.release_date == "":
            erori+= "Data lansarii este invalida!"
        if movie.imdb_rating == "" or movie.imdb_rating < 1.0 or movie.imdb_rating > 10.0:
            erori+= "Nota acordata filmului este invalida!"
        if len(erori) > 0:
            raise ValueError(erori)
