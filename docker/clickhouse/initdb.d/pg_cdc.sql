CREATE DATABASE IF NOT EXISTS pg_cdc
ENGINE = MaterializedPostgresSQL('postgres-source:5432', 'pgsource', 'pgsource', 'pgsource')
SETTINGS materialized_postgresql_tables_list = 'companies,invoices';