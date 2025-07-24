import json
import asyncio
import aiofiles

# Пример данных для записи
data = {
    "name": "Иван",
    "age": 30,
    "city": "Москва"
}

# Асинхронная функция для записи в JSON
async def write_to_json(file_path: str, data: dict):
    try:
        # Открываем файл асинхронно в режиме записи
        async with aiofiles.open(file_path, mode='w', encoding='utf-8') as file:
            # Преобразуем данные в JSON и записываем
            await file.write(json.dumps(data, ensure_ascii=False, indent=4))
            print(f"Данные успешно записаны в {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при записи: {str(e)}")

# Запуск асинхронной функции
async def main():
    file_path = 'data.json'
    await write_to_json(file_path, data)

# Запуск основного цикла событий
if __name__ == "__main__":
    asyncio.run(main())