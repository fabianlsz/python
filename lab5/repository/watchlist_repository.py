from domain.watchlist_domain import Watchlist

class WatchlistRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, watchlists):
        with open(self.file_path, "w") as file:
            for watchlist in watchlists:
                movie_ids = ";".join(map(str, watchlist.movie_ids))
                file.write(f"{watchlist.watchlist_id},{watchlist.user_id}:{movie_ids}\n")

    def load(self):
        watchlists = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    watchlist_id_user, movie_ids = line.strip().split(":")
                    watchlist_id, user_id = map(int, watchlist_id_user.split(","))
                    watchlist = Watchlist(watchlist_id, user_id)
                    if movie_ids:
                        watchlist.movie_ids = list(map(int, movie_ids.split(";")))
                    watchlists.append(watchlist)
        except FileNotFoundError:
            pass
        return watchlists