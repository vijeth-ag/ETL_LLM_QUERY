# curl -s localhost:8083/connector-plugins | jq



# "connector.class": "com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",

curl -i -X PUT -H "Accept:application/json" \
    -H  "Content-Type:application/json" http://localhost:8083/connectors/source-csv-spooldir-00/config \
    -d '{
        "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirLineDelimitedSourceConnector",
        "value.converter":"org.apache.kafka.connect.storage.StringConverter",
        "topic": "csv_stream",
        "input.path": "/data/unprocessed",
        "finished.path": "/data/processed",
        "error.path": "/data/error",
        "input.file.pattern": ".*\\.csv",
        "schema.generation.enabled":"true",
        "csv.first.row.as.header":"false"
        }'
        