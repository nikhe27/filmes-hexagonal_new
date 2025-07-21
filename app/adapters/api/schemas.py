from pydantic import BaseModel

class MovieCreateRequest(BaseModel):
    imdb_id: str
    user_opinion: str
    user_rating: int

class MovieResponse(BaseModel):
    imdb_id: str
    title: str
    year: str
    genre: str
    director: str
    plot: str
    user_opinion: str
    user_rating: int

    @classmethod
    def from_entity(cls, movie):
        return cls(
            imdb_id=movie.imdb_id,
            title=movie.title,
            year=movie.year,
            genre=movie.genre,
            director=movie.director,
            plot=movie.plot,
            user_opinion=movie.user_opinion,
            user_rating=movie.user_rating
        )
