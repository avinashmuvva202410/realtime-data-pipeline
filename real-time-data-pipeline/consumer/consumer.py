import json
import logging
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVER = 'localhost:29092'
INPUT_TOPIC = 'user-login'
OUTPUT_TOPIC = 'processed-user-login'

def process_message(message):
    
    data = json.loads(message)
    
    if 'user_id' not in data:
        logger.warning("Missing user_id in message: %s", message)
        return None
    
    processed_data = {
        'user_id': data['user_id'],
        'app_version': data['app_version'],
        'device_type': data['device_type'],
        'ip': data['ip'],
        'locale': data['locale'],
        'device_id': data['device_id'],
        'timestamp': data['timestamp']
    }
    
    logger.info("Processed message: %s", processed_data)
    return processed_data

def main():
    consumer = KafkaConsumer(
        INPUT_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='user-login-consumer'
    )
    
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    try:
        for message in consumer:
            logger.info("Received message: %s", message.value)
            processed_data = process_message(message.value)
            
            if processed_data:
                producer.send(OUTPUT_TOPIC, processed_data)
                logger.info("Sent processed data to topic '%s': %s", OUTPUT_TOPIC, processed_data)
    
    except KafkaError as e:
        logger.error("Kafka error: %s", e)
    finally:
        consumer.close()
        producer.close()

if __name__ == '__main__':
    main()
