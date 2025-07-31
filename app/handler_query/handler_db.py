from sqlalchemy.future import select

from app.database.db_session import get_db
from app.models.models import Game, Provider
from app.search_schems import SearchResult



async def search_get_db(query: str) -> SearchResult:
    result = SearchResult()
    try:
        async for db in get_db():

            some_query_games = select(Game.id, Game.provider_id).where(Game.title.ilike(f"%{query}%"))
            games_result = await db.execute(some_query_games)
            rows_games = games_result.all()
            if rows_games:
                games_id = set([g_id[0] for g_id in rows_games])
                providers_id = set([p_id[1] for p_id in rows_games])
                result.games, result.providers = list(games_id), list(providers_id)

            some_query_providers = select(Provider.id).where(Provider.name.ilike(f"%{query}%"))
            providers_result = await db.execute(some_query_providers)
            rows_providers = providers_result.all()
            if rows_providers:
                result.providers = [row[0] for row in providers_result if row[0] is not result.provider_id]

    except Exception as ex:
        print(ex)
    return result