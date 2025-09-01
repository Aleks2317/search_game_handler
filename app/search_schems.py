from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    games: list[int] = []
    providers: list[int] = []


class QueryUser(BaseModel):
    query: str = Field(
        min_length=2,
        max_length=100,
        description="Поисковый запрос пользователя",
    )
