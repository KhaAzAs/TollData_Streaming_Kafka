# Streaming Toll Data Pipelines using Kafka with Python
## Scenario
I am a data engineer at a data analytics consulting company. I have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. As a vehicle passes a toll plaza, the vehicle’s data like vehicle_id, vehicle_type, toll_plaza_id and timestamp are streamed to Kafka. My job is to create a data pipe line that collects the streaming data and loads it into a database.

## Objectives
In this assignment I will create a streaming data pipe by performing these steps:
- Start a MySQL Database server.
- Create a table to hold the toll data.
- Start the Kafka server.
- Install the Kafka python driver.
- Install the MySQL python driver.
- Create a topic named toll in kafka.
- Download streaming data generator program.
- Customize the generator program to steam to toll topic.
- Download and customise streaming data consumer.
- Customize the consumer program to write into a MySQL database table.
- Verify that streamed data is being collected in the database table.

## Process Steps
### Start Kafka
![Start Kafka](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/start_kafka.png)
### Start Zookeeper
![Start Zookeeper](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/start_zookeeper.png)
### Create Toll topic
![Create Toll topic](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/create_toll_topic.png)
### Start simulation Toll streaming data
![Start simulation Toll streaming data](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/simulator_output.png)
### Read simulation Toll stream data
![Read simulation Toll stream data](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/data_reader_output.png)
### Data stream to Database (MySQL)
![Data stream to Database (MySQL)](https://raw.githubusercontent.com/KhaAzAs/tolldata_streaming_kafka/main/output_row.png)
