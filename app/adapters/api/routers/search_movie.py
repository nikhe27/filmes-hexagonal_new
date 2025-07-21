from fastapi import APIRouter, HTTPException, Query
from infrastructure.database.repository.movie_repository import MovieRepository
from adapters.api.schemas import MovieResponse

router = APIRouter()

@router.get("/search-movie", response_model=list[MovieResponse])
def search_movie(title: str = Query(..., description="Título do filme")):
    repository = MovieRepository()
    try:
        results = repository.search_by_title(title)
        if not results:
            raise HTTPException(status_code=404, detail="Nenhum filme encontrado")
        return [MovieResponse.from_entity(movie) for movie in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
