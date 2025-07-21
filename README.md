# 🎬 Filmes Hexagonal API

API desenvolvida com **FastAPI**, **Arquitetura Hexagonal**, **DDD** e princípios de **Clean Architecture**. Permite criar e buscar filmes com avaliações personalizadas.

---

## 📁 Estrutura do Projeto

```
app/
├── adapters/                    # Interface de entrada e saída
│   └── api/
│       ├── routers/             # Rotas da API
│       │   ├── create_movie.py
│       │   └── search_movie.py
│       └── schemas.py           # Schemas Pydantic (Request/Response)
├── application/                 # Casos de uso
│   └── use_cases/
│       └── create_movie_use_case.py
├── domain/                      # Entidades de negócio
│   └── entities/
│       └── movie.py
├── infrastructure/             # Implementações técnicas
│   └── database/
│       └── repository/
│           ├── __init__.py
│           └── movie_repository.py
main.py                          # Instância da FastAPI e registro das rotas
```

---

## 🚀 Como executar o projeto

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos:

```bash
# Subir os containers
docker-compose up --build -d

# Acompanhar os logs
docker logs -f filmes-hexagonal_new-app-1
```

A API estará disponível em:  
**[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 🔍 Como testar os endpoints

### 📮 POST /create-movie

Cria um novo filme com dados da OMDb e avaliação personalizada.

**Payload de exemplo:**
```json
{
  "imdb_id": "tt0133093",
  "user_opinion": "Um clássico da ficção científica!",
  "user_rating": 10
}
```

---

### 🔎 GET /search-movie

Busca filmes mockados por título:

**Exemplo de chamada:**
```
GET /search-movie?title=Matrix
```

**Resposta mockada:**
```json
[
  {
    "imdb_id": "tt0133093",
    "title": "The Matrix",
    "year": "1999",
    "genre": "Action, Sci-Fi",
    "director": "The Wachowskis",
    "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality.",
    "user_opinion": "Muito bom!",
    "user_rating": 9
  }
]
```

---

## 🧠 Tecnologias e padrões utilizados

- ✅ FastAPI
- ✅ Docker e Docker Compose
- ✅ Arquitetura Hexagonal
- ✅ Domain-Driven Design (DDD)
- ✅ Clean Architecture
- ✅ Pydantic
- ✅ Uvicorn

---

## 💬 Observações

- A API está preparada para ser expandida com banco de dados real e integração completa com OMDb.
- Por enquanto, `search_by_title()` retorna dados mockados.

---

Desenvolvido por Monique Zanella 🤘🖤
