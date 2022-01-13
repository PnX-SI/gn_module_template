-- Script to remove schema and all data linked in GeoNature DB
BEGIN;

\echo '--------------------------------------------------------------------------------'
\echo 'SHT schema'
\echo 'Delete cascade SHT schema'
DROP SCHEMA IF EXISTS :moduleSchema CASCADE ;


-- Supprimer, si nécessaire, les éléments par défaut ajouter à la base de GN,
-- par exemple des nomenclatures.


\echo '--------------------------------------------------------------------------------'
\echo 'GN COMMONS'

\echo 'Unlink module from dataset'
DELETE FROM gn_commons.cor_module_dataset
    WHERE id_module = (
        SELECT id_module
        FROM gn_commons.t_modules
        WHERE module_code ILIKE :'moduleCode'
    ) ;

\echo 'Uninstall module (unlink this module of GeoNature)'
DELETE FROM gn_commons.t_modules
    WHERE module_code ILIKE :'moduleCode' ;

\echo '----------------------------------------------------------------------------'
\echo 'COMMIT if all is ok:'
COMMIT;
