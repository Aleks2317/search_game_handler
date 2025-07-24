import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST=os.getenv("REDIS_HOST")
# REDIS_PASSWORD,
REDIS_PORT=os.getenv("REDIS_PORT")

KAFKA_BOOTSTRAP_SERVERS=os.getenv("KAFKA_BOOTSTRAP_SERVERS")
REQUEST_TOPIC=os.getenv("REQUEST_TOPIC")
ANSWER_TOPIC=os.getenv("ANSWER_TOPIC")