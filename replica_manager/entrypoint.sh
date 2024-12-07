#!/bin/bash

# Get the number of replicas to create from the environment variable
REPLICA_COUNT=${REPLICA_COUNT:-3}  # Default to 3 replicas if not provided

echo "Creating $REPLICA_COUNT replicas..."

# Loop to create the specified number of replicas
for i in $(seq 1 $REPLICA_COUNT)
do
  REPLICA_NAME="postgres_replica_$i"
  echo "Creating replica: $REPLICA_NAME"

  # Run the command to create a new replica container
  docker run -d --name $REPLICA_NAME \
    --link postgres_primary:postgres_primary \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=datawarehouse \
    -e POSTGRES_PRIMARY_HOST=postgres_primary \
    postgres:latest
  
  # Add any replication-specific configuration here
  docker exec $REPLICA_NAME bash -c "
    pg_basebackup -h postgres_primary -D /var/lib/postgresql/data -U replicator -v -P
    echo 'primary_conninfo = \"host=postgres_primary port=5432 user=replicator password=replica_password\"' >> /var/lib/postgresql/data/postgresql.conf.sample
    pg_ctl -D /var/lib/postgresql/data -l logfile start
  "

done

echo "Replicas created."
