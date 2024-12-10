from domain.validation import Validation
from repository.user_repository import UserRepository
from repository.watchlist_repository import WatchlistRepository
from service.service_watchlist import ServiceWatchlist
from repository.movie_repository import MovieRepository

def show_watchlist_menu():
    print("\nWatchlist Management Menu:")
    print("1. Add a movie to a user's watchlist")
    print("2. Edit a watchlist")
    print("3. Filter movies by actor")
    print("4. Filter movies by IMDb rating")
    print("5. Count movies an actor appeared in")
    print("6. Calculate the average IMDb rating of movies an actor appeared in")
    print("7. Show all watchlists")
    print("8. Exit")

def add_watchlist(service):
    try:
        user_id = int(input("Enter the user ID: "))
        movie_ids = list(map(int, input("Enter movie IDs (comma-separated): ").split(",")))
        service.add_watchlist(user_id, movie_ids)
        print("Watchlist added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def edit_watchlist(service):
    try:
        watchlist_id = int(input("Enter the watchlist ID to edit: "))
        movie_ids = list(map(int, input("Enter new movie IDs (comma-separated): ").split(",")))
        service.update_watchlist(watchlist_id, movie_ids)
        print("Watchlist updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def filter_movies_by_actor(service):
    actor = input("Enter the actor's name: ")
    filtered_movies = service.filter_movies_by_actor(actor)
    if not filtered_movies:
        print("No movies found with this actor.")
    else:
        print("Movies featuring", actor, ":")
        for movie in filtered_movies:
            print(movie)

def filter_movies_by_rating(service):
    try:
        rating = float(input("Enter the minimum IMDb rating: "))
        filtered_movies = service.filter_movies_by_rating(rating)
        if not filtered_movies:
            print("No movies found with a rating above this value.")
        else:
            print("Movies with IMDb rating above", rating, ":")
            for movie in filtered_movies:
                print(movie)
    except ValueError as e:
        print(f"Error: {e}")

def count_movies_by_actor(service):
    actor = input("Enter the actor's name: ")
    count = service.count_movies_by_actor(actor)
    print(f"{actor} appeared in {count} movie(s).")

def calculate_avg_rating_by_actor(service):
    actor = input("Enter the actor's name: ")
    avg_rating = service.average_rating_by_actor(actor)
    if avg_rating == 0:
        print(f"No movies found featuring {actor}.")
    else:
        print(f"The average IMDb rating of movies featuring {actor} is {avg_rating:.2f}.")

def show_all_watchlists(service):
    watchlists = service.get_watchlists()
    if not watchlists:
        print("No watchlists available.")
    else:
        for watchlist in watchlists:
            print(watchlist)

def main():
    movie_repo = MovieRepository("movies.txt")
    validator = Validation()
    user_repo = UserRepository("users.txt")
    watchlist_repo = WatchlistRepository("watchlists.txt")
    watchlist_service = ServiceWatchlist(validator,watchlist_repo, movie_repo, user_repo)

    while True:
        show_watchlist_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_watchlist(watchlist_service)
        elif choice == "2":
            edit_watchlist(watchlist_service)
        elif choice == "3":
            filter_movies_by_actor(watchlist_service)
        elif choice == "4":
            filter_movies_by_rating(watchlist_service)
        elif choice == "5":
            count_movies_by_actor(watchlist_service)
        elif choice == "6":
            calculate_avg_rating_by_actor(watchlist_service)
        elif choice == "7":
            show_all_watchlists(watchlist_service)
        elif choice == "8":
            print("Exiting Watchlist Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
