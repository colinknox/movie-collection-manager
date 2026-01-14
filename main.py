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
            if current_movie.year == year:
                movie_by_year.append(current_movie)

        return movie_by_year

    def search_collection(self, search_string):
        movies_in_search = []
        
        for current_movie in self.movie_list:
            if search_string.lower() in current_movie.title.lower() or search_string.lower() in current_movie.director.lower() or search_string.lower() in current_movie.genre.lower():
                movies_in_search.append(current_movie)

        return movies_in_search



collection = MovieCollection("John")
collection.add_movie(Movie("Dune", "Denis Villeneuve", 2021, "Sci-Fi"))
collection.add_movie(Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi"))

print(collection.search_collection("sci"))  # Should return both (genre match)
print(collection.find_by_year(2021))  # Should return only Dune
