from aiokafka import AIOKafkaConsumer

from app.settings import KAFKA_BOOTSTRAP_SERVERS, REQUEST_TOPIC


class Consumer:
    def __init__(
            self,
            auto_offset_reset: str = "earliest",
            enable_auto_commit: bool = True,
    ):
        self.bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS
        self.group_id = 'my-group'
        self.topics = [REQUEST_TOPIC]
        self.auto_offset_reset = auto_offset_reset
        self.enable_auto_commit = enable_auto_commit
        self.consumer = None


    async def start(self):
        try:
            self.consumer = AIOKafkaConsumer(
                *self.topics,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                auto_offset_reset=self.auto_offset_reset,
                enable_auto_commit=self.enable_auto_commit,
            )
            await self.consumer.start()
            print("Потребитель успешно подключен")
        except Exception as e:
            print(f"Ошибка подключения: {e}")


    async def stop(self):
        if self.consumer:
            await self.consumer.stop()
            print("Потребитель остановлен")


consumer_worker = Consumer()
