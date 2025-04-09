from pyflink.table import TableEnvironment, EnvironmentSettings

env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
env.get_config().set("parallelism.default", "1")

env.execute_sql("""
    CREATE TABLE foobar (
        ts TIMESTAMP(3)
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'foobar',
        'properties.bootstrap.servers' = 'kafka:9092',
        'properties.group.id' = 'flink-consumer-group',
        'scan.startup.mode' = 'latest-offset',
        'format' = 'json',
        'json.fail-on-missing-field' = 'false',
        'json.timestamp-format.standard' = 'ISO-8601'
    )
""")

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
        'format' = 'json',
        'json.timestamp-format.standard' = 'ISO-8601'
    )
""")

# Execute the transformation and insert into the sink table
env.execute_sql("""
    INSERT INTO foobar_split
    SELECT 
        ts,
        EXTRACT(YEAR FROM ts) AS ts_year,
        EXTRACT(MONTH FROM ts) AS ts_month,
        EXTRACT(DAY FROM ts) AS ts_day,
        EXTRACT(HOUR FROM ts) AS ts_hour,
        EXTRACT(MINUTE FROM ts) AS ts_minute,
        EXTRACT(SECOND FROM ts) AS ts_second
    FROM foobar
""")

