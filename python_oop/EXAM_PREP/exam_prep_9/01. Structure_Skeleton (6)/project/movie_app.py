from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.user_usernames = []

    def register_user(self, username: str, age: int):
        usernames = [u.username for u in self.users_collection]
        if username in usernames:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        self.user_usernames.append(username)
        return f"{username} registered successfully."

    def check_if_user_exists(self, username):

        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def upload_movie(self, username: str, movie: Movie):
        usernames = [u.username for u in self.users_collection]
        if username not in usernames:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self.find_user_by_name(username)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            if key == 'year':
                movie.year = value
            if key == 'age_restriction':
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        res = []
        for m in sorted_movies:
            res.append(m.details())

        if res:
            return '\n'.join(res)

        return "No movies found."

    def __str__(self):
        users = ', '.join([u.username for u in self.users_collection])
        movies = ', '.join([m.title for m in self.movies_collection])

        return f'All users: {users if users else "No users."}\n'\
                f'All movies: {movies if movies else "No movies."}'

    def find_user_by_name(self, name):
        user = [u for u in self.users_collection if u.username == name][0]

        return user
