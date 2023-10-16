# Template de création d'un module GeoNature

Ce template décrit la structure obligatoire d'un module GeoNature.

- Le backend est développé en Python grâce au framework Flask.
- Le frontend est développé grâce au framework Angular (voir la version actuelle du coeur de GeoNature)

GeoNature prévoit cependant l'intégration de module "externe" dont le frontend serait développé dans d'autres technologies. La gestion de l'intégration du module est à la charge du développeur.

## Génération d'un module à l'aide de ![Alt text](https://raw.githubusercontent.com/cookiecutter/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png)

Pour générer le squelette d'un module externe de Geonature, nous proposons d'utiliser `cookiecutter`. Cookiecutter est une librairie python permettant de produire une arborescence de fichier ainsi que leur contenu à l'aide d'un template.

Installer `cookiecutter` à l'aide de la commande suivante:

```{shell}
pip install cookiecutter
```

Une fois installé, lancer la commande suivante dans le terminal:

```{shell}
cookiecutter gh:PnX-SI/gn_module_template -c cookiecutter-generation
```

## Documentation :

- Développer un module GeoNature : https://docs.geonature.fr/development.html#developper-un-module-externe
- Installer un module GeoNature : https://docs.geonature.fr/installation.html#installation-d-un-module-geonature

### Fichiers relatifs au bon fonctionnement du module

### Backend

Voir https://github.com/PnX-SI/GeoNature/issues/1272

### Frontend

Le dossier `frontend` comprend les élements suivants :

- le dossier `app` comprend le code typescript du module

  - Il doit inclure le "module Angular racine", celui-ci doit impérativement s'appeler `gnModule.module.ts`

- le dossier `assets` avec l'ensemble des médias (images, son).
- Un fichier `package.json` qui décrit l'ensemble des librairies JS nécessaires au module.
