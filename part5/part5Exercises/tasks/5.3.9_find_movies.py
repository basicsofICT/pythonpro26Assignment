"""
5.3.9 Find movies

Please write a function named find_movies(database: list, search_term: str), which 
searches for movies by name in a movie database.

The function should return a list containing all movies whose name contains the 
search term. The search should not be case-sensitive, so the search term "python" 
should match both "Python" and "python".

Example:
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
                {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
                {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)

Expected output:
    [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, 
     {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
"""

# TODO: Implement your solution below this line

