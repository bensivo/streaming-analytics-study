from kafka import KafkaProducer
import json
import datetime
import time


def main():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    for _ in range(10):

        payload = json.dumps({
            'ts': datetime.datetime.now().isoformat()
        })
        print(f'Producing: {payload}')
        payload_bytes = payload.encode('utf-8')
        producer.send('foobar', payload_bytes)
        time.sleep(1)

if __name__ == "__main__":
    main()
