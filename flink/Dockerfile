# A Custom flink docker image, which uses the same version of flink
# as our local flink cluster, but also has an installation of Python3
# with some basic flink libraries.
#
# This image is used to submit pyflink jobs to the flink cluster
#
FROM apache/flink:1.19.0-scala_2.12-java17

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Make sure we use Python 3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set up Python environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install PyFlink and other Python dependencies
RUN pip3 install --no-cache-dir \
    apache-flink \
    apache-flink-libraries \
    pandas \
    numpy \
    requests \
    ruamel.yaml

# Download Kafka connector (adjust version as needed)
RUN curl -O https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.3.0-1.19/flink-sql-connector-kafka-3.3.0-1.19.jar && \
    mv flink-sql-connector-kafka-3.3.0-1.19.jar ${FLINK_HOME}/lib/

# Download JDBC connector + postgres driver
RUN curl -O https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-jdbc/3.2.0-1.19/flink-connector-jdbc-3.2.0-1.19.jar && \
    mv flink-connector-jdbc-3.2.0-1.19.jar ${FLINK_HOME}/lib/

RUN curl -O https://jdbc.postgresql.org/download/postgresql-42.7.5.jar && \
    mv postgresql-42.7.5.jar ${FLINK_HOME}/lib/

