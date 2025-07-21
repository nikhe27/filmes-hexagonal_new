from fastapi import APIRouter, HTTPException
from domain.entities.movie import Movie
from infrastructure.database.repository.movie_repository import MovieRepository
from application.use_cases.create_movie_use_case import CreateMovieUseCase
from adapters.api.schemas import MovieCreateRequest, MovieResponse

router = APIRouter()

@router.post("/create-movie", response_model=MovieResponse)
def create_movie(request: MovieCreateRequest):
    repository = MovieRepository()
    use_case = CreateMovieUseCase(repository=repository)

    try:
        movie = use_case.execute(
            imdb_id=request.imdb_id,
            user_opinion=request.user_opinion,
            user_rating=request.user_rating
        )
        return MovieResponse.from_entity(movie)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
