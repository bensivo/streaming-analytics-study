list:
    just list

build:
    podman build -t producer ./producer --file ./producer/Dockerfile
    podman build -t flink ./flink --file ./flink/Dockerfile

kafka:
    podman compose up -d kafka kafka-ui
    open http://localhost:8080

producer:
    podman compose up producer

flink:
    podman compose up -d flink-jobmanager flink-taskmanager
    open http://localhost:8081

flink-submit:
    podman run --network streaming-analytics-study_default -it -v ./flink-jobs:/flink-jobs flink flink run \
        -m flink-jobmanager:8081 \
        -py /flink-jobs/foobar-split.py \
        -j /opt/flink/lib/flink-sql-connector-kafka-3.3.0-1.19.jar

flink-submit-sink:
    podman run --network streaming-analytics-study_default -it -v ./flink-jobs:/flink-jobs flink flink run \
        -m flink-jobmanager:8081 \
        -py /flink-jobs/postgres-sink.py \
        -j /opt/flink/lib/flink-sql-connector-kafka-3.3.0-1.19.jar \
        -j /opt/flink/lib/flink-connector-jdbc-3.2.0-1.19.jar \
        -j /opt/flink/lib/postgresql-42.7.5.jar 

postgres:
    podman compose up -d postgres

down:
    podman compose down

