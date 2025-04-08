# streaming-analytics-study

A personal study on streaming analytics technologies.


## Running

1. Build all docker images:
    ```
    just build
    ```

2. Start a single-node apache kafka cluster, and "kafka-ui"
    ```
    just kafka
    ```

    Your browser will open to localhost:8080 with the kafka-ui webpage. You can use this webapp
    to produce and consume messages to/from the kafka cluster


3. Start the producer
    ```
    just producer
    ```
