import json
import logging
import time
from kafka import KafkaProducer
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVER = 'localhost:29092'
TOPIC = 'user-login'

def create_message():
    """
    Create a sample user login message.
    """
    message = {
        "user_id": str(uuid.uuid4()), 
        "app_version": "2.3.0",
        "device_type": "android",
        "ip": "199.172.111.135",
        "locale": "RU",
        "device_id": "593-47-5928",
        "timestamp": str(int(time.time())) 

    return message

def main():
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    try:
        while True:
            message = create_message()
            producer.send(TOPIC, message)
            logger.info("Sent message to topic '%s': %s", TOPIC, message)
            time.sleep(1)

    except Exception as e:
        logger.error("Error producing message: %s", e)
    finally:
        producer.close()

if __name__ == '__main__':
    main()
