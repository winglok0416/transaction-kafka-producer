from kafka import KafkaProducer


class TransactionRecordProducer:
    def __init__(self):
        self.topic = "transaction"
        self.producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])

    def publish(self, key, value):
        future = self.producer.send(
            topic=self.topic,
            key=key.encode('UTF-8'),
            value=value.encode('UTF-8'),
            partition=0)
        result = future.get(10)
        print("Published message with value: " + value)
        return result
