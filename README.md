# Filmes Hexagonal API 

Este projeto é uma API que simula um sistema de cadastro e busca de filmes, feita em **Python com FastAPI**, seguindo princípios modernos de arquitetura como:

- Arquitetura Hexagonal
- Domain-Driven Design (DDD
- Clean Architecture**
-  Tudo dockerizado pra facilitar

---

## O que essa API faz

Ela tem **duas funcionalidades principais**:

1. **Criar um filme** com base em um IMDb ID, uma nota e sua opinião pessoal.
2. **Buscar filmes** pelo título (simulado, com dados mockados por enquanto).

> Os dados dos filmes (título, diretor, etc.) são preenchidos automaticamente com valores fictícios simulando uma integração com a OMDb.

---

## ▶️ Como rodar esse projeto

1. Tenha **Docker e Docker Compose** instalados.
2. No terminal, vá até a raiz do projeto e rode:

```bash
docker-compose up --build -d
```

3. Espere até o log mostrar:

```
Uvicorn running on http://0.0.0.0:8000
```

4. Vá para o navegador e acesse:
```
http://localhost:8000/docs
```

Você vai ver a interface de testes do FastAPI (Swagger UI).

---

##  Como testar a API sem erro

###  Teste 1: Criar um filme

1. No Swagger, clique em `POST /create-movie`
2. Clique em **"Try it out"**
3. No corpo da requisição (Request body), cole isso:

```json
{
  "imdb_id": "tt0133093",
  "user_opinion": "Um clássico da ficção científica!",
  "user_rating": 10
}
```

4. Clique em **"Execute"**

Se tudo estiver certo, você vai ver uma resposta como esta:

```json
{
  "imdb_id": "tt0133093",
  "title": "The Matrix",
  "year": "1999",
  "genre": "Action, Sci-Fi",
  "director": "The Wachowskis",
  "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality.",
  "user_opinion": "Um clássico da ficção científica!",
  "user_rating": 10
}
```

> Isso significa que seu projeto está funcionando perfeitamente.

---

###  Teste 2: Buscar filmes

1. No Swagger, clique em `GET /search-movie`
2. Clique em **"Try it out"**
3. No campo `title`, digite:

```
Matrix
```

4. Clique em **"Execute"**

Você verá uma lista com um único filme mockado do Matrix.

---

##  Observações

- O projeto está pronto para crescer: você pode facilmente integrar com banco de dados, autenticação, OMDb real, etc.
- Por enquanto, todos os dados retornados são simulações feitas internamente (mock).

---

Desenvolvido por Monique 
