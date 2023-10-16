Template de création d'un module GeoNature
==========================================

Ce template décrit la structure obligatoire d'un module GeoNature.

- Le backend est développé en Python grâce au framework Flask.
- Le frontend est développé grâce au framework Angular (voir la version actuelle du coeur de GeoNature)

GeoNature prévoit cependant l'intégration de module "externe" dont le frontend serait développé dans d'autres technologies. La gestion de l'intégration du module est à la charge du développeur.

Documentation : 

- Développer un module GeoNature : https://docs.geonature.fr/development.html#developper-un-module-externe
- Installer un module GeoNature : https://docs.geonature.fr/installation.html#installation-d-un-module-geonature

Génération du template à l'aide de cookiecutter
===============================================

Pour générer le squelette de votre module, il faut utiliser `cookiecutter`.

Installer ``cookiecutter`` à l'aide de la commande suivante:

  pip install cookiecutter

Une fois installé, lancer la commande suivante dans le terminal:

  cookiecutter gh:PnX-SI/gn_module_template -c cookiecutter-generation

Fichiers relatifs au bon fonctionnement du module
=================================================

Backend
-------

Voir https://github.com/PnX-SI/GeoNature/issues/1272

Frontend
--------

Le dossier ``frontend`` comprend les élements suivants :

- le dossier ``app`` comprend le code typescript du module

  - Il doit inclure le "module Angular racine", celui-ci doit impérativement s'appeler ``gnModule.module.ts`` 

- le dossier ``assets`` avec l'ensemble des médias (images, son).
    
- Un fichier ``package.json`` qui décrit l'ensemble des librairies JS nécessaires au module.
