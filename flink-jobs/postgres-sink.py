from pyflink.table import TableEnvironment, EnvironmentSettings

env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
env.get_config().set("parallelism.default", "1")

# NOTE: we need to re-execute the CREATE TABLE statement, beacuse
# we're not using something like a hive metastore
env.execute_sql("""
    CREATE TABLE foobar_split (
        ts TIMESTAMP(3),
        ts_year BIGINT,
        ts_month BIGINT,
        ts_day BIGINT,
        ts_hour BIGINT,
        ts_minute BIGINT,
        ts_second BIGINT
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'foobar_split',
        'properties.bootstrap.servers' = 'kafka:9092',
        'properties.group.id' = 'flink-postgres-sink',
        'format' = 'json',
        'json.timestamp-format.standard' = 'ISO-8601'
    )
""")


env.execute_sql("""
    CREATE TABLE foobar_split_postgres (
        ts TIMESTAMP(3),
        ts_year BIGINT,
        ts_month BIGINT,
        ts_day BIGINT,
        ts_hour BIGINT,
        ts_minute BIGINT,
        ts_second BIGINT
    ) WITH (
        'connector' = 'jdbc',
        'url' = 'jdbc:postgresql://postgres:5432/streaming_analytics_study',
        'username' = 'username',
        'password' = 'password',
        'table-name' = 'foobar_split'
    )
""")

env.execute_sql("""
    INSERT INTO foobar_split_postgres
    SELECT * FROM foobar_split
""")

