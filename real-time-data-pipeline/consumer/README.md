# Kafka Consumer

This is a simple Kafka consumer that reads user login messages from the `user-login` topic,
processes them, and sends the processed data to the `processed-user-login` topic.

## Requirements

- Python 3.x
- Kafka and Zookeeper running

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
