from kafka import KafkaProducer


class KafkaProducers():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def send(self, topic, message):
        v = {
            'msg': {
                message
            },
        }
        self.producer.send(topic, v)
