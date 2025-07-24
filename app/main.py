import asyncio
import json

from consumer import consumer
from search_schems import SearchResponse, QueryUser


def write_bd(response: dict):
    try:
        with open('db.json', mode='a', encoding='utf-8') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)
            print(f"Данные успешно записаны в db.json")
    except Exception as e:
        print(f"Произошла ошибка при записи: {str(e)}")



async def main():
    await consumer.start()
    try:
        async for message in consumer.consumer:
            try:
                msg_str = message.value.decode('utf-8')
                message = json.loads(msg_str)
                # здесь должен быть код обращения к smtp-серверу
                print(f'попытка записи сообщение: {QueryUser.model_validate_json(msg_str)}')
                write_bd(message)
                print(f'Отправлено сообщение: {QueryUser.model_validate_json(msg_str)}')
            except Exception as e:
                print(f"Ошибка обработки сообщения: {e}")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
    finally:
        await consumer.stop()



if __name__ == "__main__":
    asyncio.run(main())