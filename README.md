# streaming-analytics-study

A personal study on streaming analytics technologies, specifically Kafka and Flink.


## Running

1. Build all docker images:
    ```
    just build
    ```

2. Start a single-node apache kafka cluster, and "kafka-ui"
    ```
    just kafka
    ```

    Your browser will open to http://localhost:8080 with the kafka-ui webpage. You can use this webapp
    to produce and consume messages.

    In kafka-ui, create 2 topics: 'foobar' and 'foobar_split'.


3. Start the flink cluster
    ```
    just flink
    ```

    Your browser will open to the flink UI, at http://localhost:8081. It may take a while to come up.


4. Submit the foobar-split.py flink job to the cluster
    ```
    just flink-submit
    ```

    You should see the job submitted in the flink ui. It should appear in 'Running Jobs'.

6. Then run the producer with:
    ```
    just producer
    ```

    The producer sends messages to the topic 'foobar' with a simple ISO8601 timestamp. NOTE: it'll only send 10 messages.


7. Watch messages on foobar_split.

    The flink job should read these messages, extract the components of the ts, and push
    new messages to 'foobar_split'
    
    In the kafka-ui webapp, go to the 'foobar_split' topic, then 'messages', then switch the mode to "LIVE" to see messages come in in real-time.

