from movie_domain import Movie
from user_domain import User


class Validation:
    def validator_user(self, user: User):
        erori = ""
        if user.get_name() == "":
            erori += "Nume invalid! "
        if user.get_age() == "":
            erori += "Varsta invalida! "
        if len(erori) > 0:
            raise ValueError(erori)

    def validator_movie(self, movie: Movie):
        erori = ""
        if movie.get_title() == "":
            erori += "Titlu invalid!"
        if movie.get_actors() == "":
            erori += "Actori invalizi!"
        if movie.get_release_date() == "":
            erori+= "Data lansarii este invalida!"
        if movie.get_imdb_rating() == "" or movie.get_imdb_rating() < 1.0 or movie.get_imdb_rating() > 10.0:
            erori+= "Nota acordata filmului este invalida!"
        if len(erori) > 0:
            raise ValueError(erori)
