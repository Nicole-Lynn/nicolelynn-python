# MOVIE MATCHMAKER

#### Video Demo:  https://youtu.be/fZucU_y-zcc

## Description
The final project is a terminal-based movie suggesting program made using Python programming language. The program leverages a
movie database API's genre and the top 100 popular movies data to provide tailored movie recommendations. Based on a user's
choice of genre, the program gives the user suggestions of movies with that genre. For the movies, the available
information provided for each movie by the program include:
- `Title` - The title of the movie.
- `Genres` - All the genres that are in specific movie. A movie has at least one genre.
- `Release Date` - The date that the movie was released, that is, the year, the month and the day.
- `Overview` - An overview, a brief summary of what the movie is about.


The program utilizes __time__ module that is a built in module in python and pip installable libraries : __pytest__, __requests__ and __tabulate__.
It consists of a main function and five other subprograms/functions: `available_genres`, `make_choice`,
`get_genre_by_index`, `get_genre_by_name` and `get_movies`. These functions are called from the main function in the respective
order to control the flow.


### Features
- Genre Retrieval : Fetching the available genres from the API.
- Genre Choice Options : The user has an option of picking a genre from a list of available genres by either typing in the name
of the genre or by its prefixed index.
- Popular Movie Suggestions : Retrieves and displays popular movies for the selected genre, helping users discover both new
releases and beloved classics.
- Up-to-Date Information : Utilizing an API ensures that the movie suggestions are always current and relevant.
- Scalability : Design adapts to new genres as they are added to the database, offering an ever growing library of options.
Changes in movies ranking are considered and reflect in case of rank changes.

### Project Structure (Files):
- project.py contains the main program in Python.
- test_project.py contains unit tests for functions in the main program, `project.py`. Unit tests are for the functions `available_genres`, `get_genre_by_index` and `get_genre_by_name`.
- requirements.txt which contains names of the pip installable libraries that the project requires.
- README.md for the project overview.

## Usage
To run the program, execute the command:

```python project.py```

Follow the prompts on screen to select a genre and get movie suggestions.



## Acknowledgements
The data used in this project is obtained from [The Movie Database (TMDB)](https://www.themoviedb.org/) API.


