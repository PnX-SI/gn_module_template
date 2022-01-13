Template de création d'un module GeoNature
==========================================

Ce template décrit la structure obligatoire d'un module GeoNature.

- Le backend est développé en Python grâce au framework Flask.
- Le frontend est développé grâce au framework Angular (voir la version actuelle du coeur)

GeoNature prévoit cependant l'intégration de module "externe" dont le frontend
serait développé dans d'autres technologies. La gestion de l'intégration du
module est à la charge du développeur.

Documentation :

- Développer un module GeoNature : http://docs.geonature.fr/development.html#developper-un-gn-module
- Installer un module GeoNature : http://docs.geonature.fr/development.html#installer-un-gn-module

Fichiers relatifs à l'installation
==================================

* ``manifest.tml`` (obligatoire) : Fichier contenant la description du
module (nom, version de GeoNature supportée ...)
* ``bin/install_env.sh`` (optionnel) : Installation des paquets Debian.
* ``bin/install_db.sh``  (optionnel) : Installation d'installation du schéma de BDD du
module. Non obligatoire car le module peut être piloté par le code.
* ``bin/install_app.sh`` (optionnel) : Si besoin de manipulation sur le serveur
(copie de fichier, desample ...)
* ``install_gn_module.py`` (obligatoire) : Fichier d'installation du module :
  * commandes SQL
  * extra commandes python
  * ce fichier doit contenir la méthode suivante : ``gnmodule_install_app(gn_db, gn_app)``
* ``backend/requirements.txt`` : Liste des paquets Python nécessaire au module.
* ``config/conf_schema_toml.py`` : Schéma Marshmallow de spécification des paramètres du module
* ``config/conf_gn_module.sample.toml`` : Fichier de configuration du module. Il est désamplé lors
de l'installation du module par le fichier ``install_gn_module.py``.


Fichiers relatifs au bon fonctionnement du module
=================================================

Backend
-------

Si votre module comporte des routes, il doit comporter le fichier suivant : ``backend/blueprint.py``
avec une variable ``blueprint`` qui contient toutes les routes

::

    blueprint = Blueprint('gn_module_validation', __name__)


Frontend
--------

Le dossier ``frontend`` comprend les élements suivants :

- le dossier ``app`` comprend le code typescript du module
  - Il doit inclure le "module Angular racine", celui-ci doit impérativement s'appeler ``gnModule.module.ts``
- le dossier ``assets`` avec l'ensemble des médias (images, son).
- Un fichier ``package.json`` qui décrit l'ensemble des librairies JS nécessaires au module.


Développement du module
=======================

Afin d'avoir l'autocomplétion du code dans votre éditeur (c'est le cas
avec Visual Studio Code), il peut être nécessaire :

- dans le dossier ``frontend/`` du module ajouter le dossier ``frontend/node_modules``
de votre installation GeoNature en tant que lien symbolique.
- ajouter dans un fichier ``frontend/package.json`` de votre module, dans
l'attribut ``devDependencies`` l'ensemble des dépendances du ``package.json``
de GeoNature.
- créer un fichier ``frontend/tsconfig.json`` avec le contenu suivant adapté à votre
installation:

```
{
    "compilerOptions": {
        "importHelpers": true,
        "outDir": "/home/user/workspace/geonature/frontend/dist/out-tsc",
        "sourceMap": true,
        "declaration": false,
        "module": "es2015",
        "moduleResolution": "node",
        "emitDecoratorMetadata": true,
        "experimentalDecorators": true,
        "target": "es5",
        "typeRoots": [
            "node_modules/@types",
            "/home/user/workspace/geonature/frontend/src/typings.d.ts"
        ],
        "lib": [
            "es2015",
            "es2016",
            "es2017",
            "dom"
        ],
        "baseUrl": "/home/user/workspace/geonature/frontend/",
        "paths": {
            "@angular/*" : ["../../gn_module_template/frontend/node_modules/@angular/*"],
            "@geonature_common/*" : ["src/app/GN2CommonModule/*"],
            "@geonature/*" : ["src/app/*"],
            "@geonature_config/*" : ["src/conf/*"],
            "@librairies/*" : ["node_modules/*"],
        }
    }
}
```
