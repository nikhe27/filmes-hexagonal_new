class Movie:
    def __init__(self, imdb_id, title, year, genre, director, plot, user_opinion, user_rating):
        self.imdb_id = imdb_id
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.plot = plot
        self.user_opinion = user_opinion
        self.user_rating = user_rating


class MovieRepository:
    def save(self, movie):
        print(f"Salvando o filme: {movie.title} com nota {movie.user_rating} e opinião: '{movie.user_opinion}'")

    def search_by_title(self, title):
        # Mock de resultado - você pode adaptar para buscar no banco ou na API do OMDb
        return [
            Movie(
                imdb_id="tt0133093",
                title="The Matrix",
                year="1999",
                genre="Action, Sci-Fi",
                director="The Wachowskis",
                plot="A computer hacker learns from mysterious rebels about the true nature of his reality.",
                user_opinion="Muito bom!",
                user_rating=9
            )
        ]
