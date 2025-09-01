import asyncio

from kafka.consumer import consumer_worker
from handler_query.handler_db import search_get_db
from services.cache import redis_cache
from search_schems import QueryUser


async def main():

    await consumer_worker.start()
    await redis_cache.init()
    try:
        async for message in consumer_worker.consumer:
            try:
                msg_str = message.value.decode("utf-8")
                msg_str = QueryUser.model_validate_json(msg_str).query
                result = await search_get_db(msg_str)
                print(f"Сообщение обработано: {result}")
                await redis_cache.set(msg_str, result.model_dump_json())
                print(f"Отправлено в Redis!")

            except Exception as e:
                print(f"Ошибка обработки сообщения: {e}")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
    finally:
        await consumer_worker.stop()


if __name__ == "__main__":
    asyncio.run(main())
