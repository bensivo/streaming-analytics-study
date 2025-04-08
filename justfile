list:
    just list

build:
    podman build -t producer ./producer --file ./producer/Dockerfile

kafka:
    podman compose up -d kafka kafka-ui
    open http://localhost:8080

producer:
    podman compose up producer

down:
    podman compose down
