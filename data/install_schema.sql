-- Create module template schema, tables, foreigns keys, ...
BEGIN;


\echo '--------------------------------------------------------------------------------'
\echo 'Set database variables'
SET client_encoding = 'UTF8' ;


\echo '--------------------------------------------------------------------------------'
\echo 'Create schema'
CREATE SCHEMA :moduleSchema ;


\echo '--------------------------------------------------------------------------------'
\echo 'Set new database variables'
SET search_path = :moduleSchema, pg_catalog, public;


\echo '--------------------------------------------------------------------------------'
\echo 'TABLES'

-- Vos tables

\echo '--------------------------------------------------------------------------------'
\echo 'FOREING KEYS'

-- Vos clés étrangères

\echo '--------------------------------------------------------------------------------'
\echo 'INDEXES'

-- Vos index

\echo '----------------------------------------------------------------------------'
\echo 'COMMIT if all is ok:'
COMMIT ;
