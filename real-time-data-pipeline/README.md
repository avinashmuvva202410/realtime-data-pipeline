# Real-Time Data Pipeline

This project implements a real-time streaming data pipeline using Kafka and Docker. The pipeline ingests user login events, processes the data, and stores the results in another Kafka topic.

## Project Structure

- `docker-compose.yml`: Docker Compose configuration file for Kafka and Zookeeper.
- `consumer/`: Contains the Kafka consumer implementation.
  - `consumer.py`: Main consumer script.
  - `requirements.txt`: Python dependencies for the consumer.
  - `README.md`: Instructions for running the consumer.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/avinashmuvva202410/realtime-data-pipeline/tree/main/real-time-data-pipeline



