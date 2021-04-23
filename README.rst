Template de création d'un module GeoNature
==========================================

Ce template décrit la structure obligatoire d'un module GeoNature.

- Le backend est développé en Python grâce au framework Flask.
- Le frontend est développé grâce au framework Angular (voir la version actuelle du coeur)

GeoNature prévoit cependant l'intégration de module "externe" dont le frontend serait développé dans d'autres technologies. La gestion de l'intégration du module est à la charge du développeur.

Documentation : 

- Développer un module GeoNature : http://docs.geonature.fr/development.html#developper-un-gn-module
- Installer un module GeoNature : http://docs.geonature.fr/development.html#installer-un-gn-module


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
