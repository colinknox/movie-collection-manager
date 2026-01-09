class Movie():
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre


class MovieCollection:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.movie_list = []

    def add_movie(self, movie):
        self.movie_list.append(movie)

    def remove_movie(self, movie):
        updated_movie_list = []

        for current_movie in self.movie_list:
            if current_movie.title != movie.title or current_movie.director != movie.director:
                updated_movie_list.append(current_movie)

        self.movie_list = updated_movie_list

        return updated_movie_list
    
    def find_by_year(self, year):
        movie_by_year = []

        for current_movie in self.movie_list:
            if current_movie.year != year:
                pass
            else:
                movie_by_year.append(current_movie)
                
        return movie_by_year

    def search_collection(self, search_string):
        searched_movies = []
        
        for current_movie in self.movie_list:
            if search_string.lower() in current_movie.title.lower() or current_movie.director.lower() or current_movie.genre.lower():
                searched_movies.append(current_movie)
        
        print(f"SEARCHED MOVIE LIST: {searched_movies}")






blade_runner = Movie("Blade Runner", "Ridley Scott", 1982, "sci-fi")
mad_max_fury_road = Movie("Mad Max: Fury Road", "George Miller", 2015, "action")
logan = Movie("Logan", "James Mangold", 2017, "action")
the_big_lebowski = Movie("The Big Lebowski", "Joel & Ethan Cohen", 1998, "comedy")
casino = Movie("Casino", "Martin Scorsese", 1995, "drama")

jack = MovieCollection("Jack")



# print(blade_runner.year)
# print(blade_runner.director)
# print(blade_runner.genre)
# print(blade_runner.title)

# print(jack.movie_list)
jack.add_movie(blade_runner)
jack.add_movie(mad_max_fury_road)
jack.add_movie(logan)
jack.add_movie(the_big_lebowski)
jack.add_movie(casino)


# jack.remove_movie(the_big_lebowski)
# print(jack.movie_list)
# jack.remove_movie(logan)
# print(jack.movie_list)

# for movie in jack.movie_list:
#     print(f"CURRENT MOVIE: {movie.title}")


jack.search_collection("blade")



# print(f"BEFORE MOVIE LIST: {jack.movie_list}")

# jack.find_by_year(1982)

# print(f"AFTER MOVIE LIST: {jack.movie_list}")