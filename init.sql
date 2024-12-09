-- -- Create replication role
-- CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'replica_password';

-- -- Allow replication connections from replica
-- host replication replicator postgres_replica_ip/32 md5

-- -- Set up the WAL (Write-Ahead Log) level for replication
-- ALTER SYSTEM SET wal_level = replica;
-- SELECT pg_reload_conf();
