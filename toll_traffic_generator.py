"""
Top Traffic Simulator
"""
# Import needed module
from time import sleep, time, ctime
from random import random, randint, choice
from kafka import KafkaProducer

# Init Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Initiate topic variable
TOPIC = 'toll'

# Generate random data to stream random simulation data
VEHICLE_TYPES = ("car", "car", "car", "car", "car", "car", "car", "car",
                 "car", "car", "car", "truck", "truck", "truck",
                 "truck", "van", "van")
for _ in range(100000):
    # Initiate random vehicle id
    vehicle_id = randint(10000, 10000000)
    # Initiate random vehicle type
    vehicle_type = choice(VEHICLE_TYPES)
    # Tracking time
    now = ctime(time())
    # Initiate random plaza id
    plaza_id = randint(4000, 4010)
    # Contruct message sent to Kafka
    message = f"{now},{vehicle_id},{vehicle_type},{plaza_id}"
    message = bytearray(message.encode("utf-8"))
    print(f"A {vehicle_type} has passed by the toll plaza {plaza_id} at {now}.")
    # Send messange to Kafka topic
    producer.send(TOPIC, message)
    sleep(random() * 2)
