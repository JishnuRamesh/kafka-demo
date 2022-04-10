#!/bin/bash

host="$1"
if [[ -z "$host" ]]; then
    echo "Using 'localhost' as host as the first parameter was not set"
    host="localhost"
fi

port="$2"
if [[ -z "$port" ]]; then
    echo "Using '8081' as port as the second parameter was not set"
    port="8081"
fi


# ADD your schemas here:

# Order schema
schema=$(tr <./dev/order.avro.json '\n' ' ' | sed -e 's/"/\\\"/g')
topic="rawevents.orders.v1"
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" --data '{"schema":"'"$schema"'"}' "http://$host:$port/subjects/$topic-value/versions"


exitCode=$?
exit $exitCode