ALTER USER default SETTINGS allow_experimental_database_materialized_postgresql = 1;

CREATE DATABASE IF NOT EXISTS pg_cdc
ENGINE = MaterializedPostgresSQL('postgres-source:5432', 'pgsource', 'pgsource', 'pgsource')
SETTINGS materialized_postgresql_tables_list = 'companies,invoices';