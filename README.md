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


3. Start the flink cluster
    ```
    just flink
    ```

    Your browser will open to the flink UI, at http://localhost:8081. It may take a while to come up.


4. Submit the flink job to the cluster
    ```
    just flink-submit
    ```

5. In kafka-ui, create 2 topics: 'foobar' and 'foobar_split'. Go to 'foobar_split', and watch messages live.

6. Then run the producer with:
    ```
    just producer
    ```
    
    You should see the messages come in to 'foobar_split', with the transformations applied.
