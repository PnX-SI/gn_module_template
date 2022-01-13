-- Insert Template Module default data (nomenclatures, module)
BEGIN ;

-- Vos données par défaut à insérer dans la base de GN, par exemple des nomenclatures.

\echo '--------------------------------------------------------------------------------'
\echo 'GN COMMONS'

\echo 'Update module infos'
UPDATE gn_commons.t_modules
SET
    module_label = 'Module Exemple',
    module_picto = 'fa-leaf',
    module_desc = 'Module d''exemple pour GeoNature en version inférieur à 2.8.1.'
WHERE module_code ILIKE :'moduleCode' ;

\echo '----------------------------------------------------------------------------'
\echo 'COMMIT if all is ok:'
COMMIT ;
