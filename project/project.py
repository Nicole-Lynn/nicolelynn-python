import requests
import time
from tabulate import tabulate


api_key = "b42907b320c1f97ffc8228c55fae9905"


# Get the list of official/available genres for movies from an API
def available_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={api_key}"
    response = requests.get(url)
    r = response.json()

    genres = [genre["name"] for genre in r["genres"]]
    return genres


# The user can make a choice whether to make a genre choice by either typing in the number, which is the index of the genre,
# or by typing in the name of the genre
def make_choice():
    print()
    print("1. Pick by number")
    print("2. Pick by name")

    while True:
        choice = input("Pick by: ")

        if not 1 <= int(choice) <= 2:
            print("Invalid choice. Pick either 1 or 2 from the given choices.")
        else:
            break
    print()

    return choice


def get_genre_by_index(g):
    genres = available_genres()

    while True:
        try:
            if not 1 <= int(g) <= 19:
                raise
            else:
                index = int(g) - 1
                genre = genres[index]
                return f"Confirmed! You chose {g} the genre, {genre.upper()}."

        except:
            print(
                "Invalid index. Kindly choose a genre number between 1 and 19 from the list above."
            )
            g = input("Choose a genre: ")


def get_genre_by_name(g):
    genres = available_genres()

    while True:
        genre = g.title()
        if genre == "Tv Movie":
            genre = "TV Movie"

        if genre not in genres:
            print(
                "Invalid genre name. Kindly choose from the list of available genres."
            )
            g = input("Choose a genre: ").title()

        else:
            break

    return f"Confirmed! You chose the genre, {genre.upper()}."


# Get the list of popular movies from the API
def get_movies():
    # GET GENRES, make a dict of genres and their unique ids from the API
    url = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={api_key}"
    genres_data = requests.get(url).json()
    ids_genres = {result["id"]: result["name"] for result in genres_data["genres"]}

    movie_data = []
    for page in range(1, 6):
        movies_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}&api_key={api_key}"
        response = requests.get(movies_url)
        movies_data = response.json()

        for result in movies_data["results"]:
            movie_titles = result["title"]
            movie_genre_ids = result["genre_ids"]
            movie_genre_names = [ids_genres[id] for id in movie_genre_ids]
            movie_genres = ", ".join(movie_genre_names)
            movie_release_dates = result["release_date"]
            movie_overviews = result["overview"]
            movie_data.append(
                {
                    "title": movie_titles,
                    "genres": movie_genres,
                    "release_date": movie_release_dates,
                    "overview": movie_overviews,
                }
            )

    return movie_data


def main():
    # To see all available genres as a listed menu
    print("Genres List:")
    genres = available_genres()
    for name in genres:
        print(genres.index(name) + 1, name, sep=".")

    # Decide whether to pick the genre by typing the name of the genre or by its prefixed index
    # Pick a genre of choice from the list of available genres using number or name
    choice = make_choice()
    selected_genre = input("Choose a genre: ")

    if choice == "1":
        genre = get_genre_by_index(selected_genre)
    elif choice == "2":
        genre = get_genre_by_name(selected_genre)

    print(genre)
    print()

    # Add a 2-second delay between the confirmation message and the suggestions
    time.sleep(2)

    for genre_name in genres:
        if genre_name.upper() in genre:
            select_genre = genre_name

    # Based on the users's genre choice, movies of the chosen genre from the popular movies list are returned
    movies = get_movies()

    if not any(select_genre in movie["genres"] for movie in movies):
        print(
            "Sorry😔. There are currently no movies in that genre that are top ranked in popular movies."
        )
        print()

    else:
        movie_suggestions = [
            {
                "Title": movie["title"],
                "Genres": movie["genres"],
                "Release Date": movie["release_date"],
                "Overview": movie["overview"],
            }
            for movie in movies
            if select_genre in movie["genres"]
        ]

        print(
            tabulate(
                movie_suggestions,
                headers="keys",
                tablefmt="grid",
                colalign=("left", "left", "left", "left"),
                maxcolwidths=[30, 20, None, 52],
            )
        )


if __name__ == "__main__":
    main()
