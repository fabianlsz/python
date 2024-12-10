from domain.watchlist_domain import Watchlist


class WatchlistRepository:
    def __init__(self, file_path):
        self.watchlists = []
        self.file_path = file_path
        self.__load()

    def __save(self):
        with open(self.file_path, "w") as file:
            for watchlist in self.get_all():
                movie_id = ";".join(map(str, watchlist.movie_ids))
                file.write(f"{watchlist.watchlist_id},{watchlist.user_id}:{movie_id}\n")

    def __load(self):
        watchlists = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    watchlist_id_user, movie_ids = line.strip().split(":")
                    watchlist_id, user_id = map(int, watchlist_id_user.split(","))
                    movie_ids_list = list(map(int, movie_ids.split(";"))) if movie_ids else []
                    watchlist = Watchlist(watchlist_id, user_id, movie_ids_list)
                    watchlists.append(watchlist)
        except FileNotFoundError:
            pass
        self.watchlists = watchlists

    def get_all(self):
        return self.watchlists

    def gen_id_watchlist(self):
        return max([e.watchlist_id for e in self.watchlists], default=0) + 1

    def find(self, watchlist_id):
        result = list(filter(lambda watchlist: watchlist.watchlist_id == watchlist_id, self.watchlists))
        return self.watchlists.index(result[0]) if result else -1

    def add(self, watchlist: Watchlist):
        if self.find(watchlist.watchlist_id) != -1:
            raise ValueError("This watchlist already exists!")
        self.watchlists.append(watchlist)
        self.__save()

    def update(self, watchlistUpdated: Watchlist):
        pos = self.find(watchlistUpdated.watchlist_id)
        if pos == -1:
            raise ValueError("The watchlist with the given ID doesn't exist!")
        self.watchlists[pos] = watchlistUpdated
        self.__save()

    def delete(self, idwatchlist: int):
        pos = self.find(idwatchlist)
        if pos == -1:
            raise ValueError("The watchlist with the given ID doesn't exist!")
        del self.watchlists[pos]
        self.__save()
