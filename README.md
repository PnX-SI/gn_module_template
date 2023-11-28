# Template de création d'un module GeoNature

GeoNature prévoit l'intégration de module "externe"et dont la gestion de l'intégration du module est à la charge du développeur.

Pour bien commencer, nous fournissons ce _template_ (ou modèle dans la langue de Molière:black_nib:) qui reprend la structure obligatoire d'un module GeoNature. Tout comme GeoNature, un module est séparé en deux parties:

1. Les compléments de l'API de GeoNature, les transferts de données avec la base PostgresSQL sont dans la partie **backend**. Ce dernier est programmé en Python et s'appuie principalement sur :
   - le framework `Flask`, un librairie permettant de créer des applications web
   - `SQLAlchemy` pour la connexion et le requêtage sur la base de données
   - `Marschmallow` pour la sérialisation d'objet python
   - `Celery` pour la gestion de tâches asynchrones
   - `alembic` pour la gestion des révisions de modifications de la base de données
2. Côté interface utilisateur (client), la partie **frontend** s'appuie sur le framework `Angular` et programmée par le trio `HTML/Javascript/CSS`. D'autres librairies sont déjà installées dans GeoNature comme :
   - `chart.js` Pour l'affichage de graphique (lineplot, scatterplot, etc.)
   - `bootstrap` Pour profiter de Bootstrap, le framework CSS
   - `leaflet` Pour l'affichage de carte interactive
   - `font-awesome` Pour avoir accès à une bibliothéque d'icônes pour tuner votre module.
   - etc.. (Voir le fichier [package.json](https://github.com/PnX-SI/GeoNature/blob/master/frontend/package.json) dans GeoNature)

<h2>Génération du squelette du module à l'aide de <img src="https://raw.githubusercontent.com/cookiecutter/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png" width="200px" /></h2>

Pour générer le squelette d'un module externe de GeoNature, nous proposons d'utiliser `cookiecutter`. 

`CookieCutter` est une librairie Python qui permet de produire une base de projet (fichiers, arborescence de dossier,..) à l'aide d'un template.

Installer `cookiecutter` à l'aide de la commande suivante:

```shell
pip install cookiecutter #requiert d'avoir une installation de python
```

Lancer la commande suivante dans le terminal pour produire la base de votre module :

```shell
cookiecutter gh:PnX-SI/gn_module_template -c cookiecutter-generation
```

Votre base de module se trouve dans le dossier avec le nom que vous avez renseigné dans `project_slug`.

## Développement du module

### Backend

#### Base de données

La gestion (connexion, requête) de la base de données de GeoNature (PostgreSQL+ PostGIS) s'effectue avec [SQLAlchemy](https://www.sqlalchemy.org/) dans sa version 1.3 (Bientôt en 2.0).

[Alembic](https://alembic.sqlalchemy.org/en/latest/) est une outil de migration de base de données développé pour SQLAlchemy. C'est avec cette outil que vous devez faire la création de vos tables, l'insertion de données initiales, etc...

Pour faire une révision, il vous suffit de créer un fichier `<key>_<label_revision>.py` dans le dossier `backend/<nom_module>/migrations`. Ce fichier doit avoir le code minimal suivant: 

```python
from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "<label_revision>"
down_revision = None # ou <label_revision_précédente_si_existe>
branch_labels = ("<nom_de_la_branche_si_première_révision",)
depends_on = None

def upgrade():
    #instruction de mise à jour de la base de données 
    


def downgrade():
    # instruction pour annuler les mises à jours apportées par la function `upgrade()`
```

**Bonne Pratique** Il est conseillé de créer une branche séparée de la principale (*geonature*) pour votre module. Pour cela, change le chaîne de caractère dans la variable `branch_labels`.

#### Gestion des migrations sur la base de données GeoNature

Lors de l'installation du module, les révisions seront installés dans la base de données GeoNature. Toutefois, il est possible d'appliquer manuellement des révisions (resp. en annuler). Pour cela, aidez-vous de la ligne de commande de GeoNature.

```shell
source <cheminVersVotreGeoNature>/backend/venv/bin/activate
geonature db upgrade # Add last revision
goenature db migrate <branchemodule>@<revisionID> # migre vers la révision d'une branche spécifique
```

#### Permissions

Depuis la version X.X.X, l'accès au module de GeoNature est régit par un système de permissions. Pour avoir accès à votre module sur Geonature, vous devez absolument avoir créer les permissions !! Parmis les révisions présentes dans ce template, le fichier `backend/migrations/<coderevision>_add_permissions.py` contient le script pour définir celle-ci. Plus précisément, il vous suffit de modifier le block de code suivant :

```sql
INSERT INTO
  gn_permissions.t_permissions_available (
      id_module,
      id_object,
      id_action,
      label,
      scope_filter
  )
SELECT
  m.id_module,
  o.id_object,
  a.id_action,
  v.label,
  v.scope_filter
FROM
  (
      VALUES
          -- Ce sont des exemples ! Ne mettez que les permissions utiles dans votre cas
          ('<codemodule>', '<codemodule>', 'C', True, 'Créer des données'),
          ('<codemodule>', '<codemodule>', 'R', True, 'Voir des données'), 
          ('<codemodule>', '<codemodule>', 'U', True, 'Modifier les données'),
          ('<codemodule>', '<codemodule>', 'V', True, 'Valider des données'),
          ('<codemodule>', '<codemodule>', 'E', True, 'Exporter des données'),
          ('<codemodule>', '<codemodule>', 'D', True, 'Supprimer des données')
  ) AS v (module_code, object_code, action_code, scope_filter, label)
JOIN
  gn_commons.t_modules m ON m.module_code = v.module_code
JOIN
  gn_permissions.t_objects o ON o.code_object = v.object_code
JOIN
  gn_permissions.bib_actions a ON a.code_action = v.action_code
```

Modifier celle-ci en fonction de vos besoins. Pour plus de détails sur les permissions, rendez-vous sur la documentation de GeoNature : https://docs.geonature.fr/admin-manual.html?highlight=permission#acces-a-geonature-et-cruved


#### Routing

[Flask](https://flask.palletsprojects.com/en/3.0.x/) est une librairie Python qui permet de faire des applications Web en Python. Une application est divisée en plusieurs "**routes**". Chaque route correspond à une activité relié à une URL. Dans l'exemple ci-dessous, l'URL `localhost/hello` retournera le résultat de la function `hello_world()`.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gdbye")
def gdbye():
    return "<p>Good Bye!</p>"
```

Pour déclarer les routes de votre module, rendez-vous dans le script `blueprint.py`. Avec Flask, il est possible de séparer les différentes routes de votre application dans différents fichiers grâce la classe `Blueprint`. 

Dans le fichier, le partie qui nous intéresse est la suivante :

```python
blueprint = Blueprint("<module_api_prefix>", __name__)
```

Dans l'exemple classique de Flask, la création d'une route requiert une fonction associée du décorateur `@app.route('nom_nouvelle_route')` de l'application Flask (variable `app`). Ici, le décorateur est différent, on doit utiliser le décorateur de l'objet Blueprint `@blueprint.route('nom_nouvelle_route')`.

**Quelle URL pour accéder aux routes définies dans blueprint.py ?** `http://<urlgeonature>/geonature/api/<code_module_en_minuscule>/<votre_route>`


#### Ajout de librairie Python

Si vous utilisez des librairies Python qui ne se trouvent pas dans les dépendances de GeoNature, indiquez celles-ci dans le fichier `requirements.in`.

### Frontend

Le frontend de GeoNature s'appuie sur le framework `Angular`. Cette section n'a pas pour but de faire un cours sur Angular mais donnez quelques pointeurs.

Si vous commencez sur Angular, les tutoriels sur la documentation officielle peuvent vous aider : https://angular.io/tutorial

#### Angular : Component, Service

Au coeur d'Angular, deux concepts essentiels nous intéressent : les classes `Component` et `Service`.

Les `Component` sont utilisés pour définir des blocks de l'UI (interface graphique). Un component est (souvent) défini dans trois fichiers :

- un fichier `nomcomponent.component.ts` qui contient le code JavaScript pour définir l'initialisation du component et son fonctionnement.
- un fichier `nomcomponent.component.scss` qui contient la feuille de style propre au component.
- un fichier `nomcomponent.component.html` qui contient le template HTML du component. Celui-ci peut être aussi défini dans le `nomcomponent.component.ts`.

La commande `ng generate component <nomcomponent>` permet générer ces fichiers nécessaires.

Comme le dit bien la documentation d'Angular, la production ou récupération de données ne doit pas être faite dans un Component !

> Les *components* ne doivent pas récupérer ou enregistrer des données directement et ils ne doivent certainement pas présenter sciemment de fausses données. Ils doivent se concentrer sur la présentation des données et déléguer l'accès aux données à un `Service`.<br><br>_Documentation Angular https://devdocs.io/angular/tutorial/tour-of-heroes/toh-pt4_

Pour créer un service, il faut soit créer le fichier vous même `mesdonnees.service.ts` avec le code suivant :

```javascript
import { Injectable } from "@angular/core";

@Injectable({ providedIn: "root" })
export class NomService {
  constructor() {}
}
```

soit en utilisant la ligne de commande de angular : `ng generate service <nomservice>`

#### Bonnes pratiques : Appel API/Backend

Utiliser l'API `@angular` pour faire des requêtes GET/PUT/POST.

```typescript
import { HttpClient } from "@angular/common/http";

export class A {
  constructor(private _client_http: HttpClient) {}
  foo() {
    this._client_http.get<Interface>("<urlAPI>"); // Iris is a TypeScript interface // Returns an observable
  }
}
```

#### Librairies GeoNature

Les librairies communes de GeoNature sont disponibles avec le prefix `@geonature_common`. Par exemple :

```javascript
import { MapComponent } from "@geonature_common/map/map.component";
```

#### Ajout de librairies

Il suffit d'ajouter celles-ci dans le `package.json` ou lancer la commande `npm install <nomlibrairie>` dans le dossier `frontend`.

### AutoComplétion dans VSCODE

#### Partie backend

Changer l'interpréteur du projet VSCODE avec celui de l'environnement virtuel `venv/bin/python` de votre instance de GeoNature.

#### Partie frontend

L'accès au librairie installée avec GeoNature ne sont pas accessible automatiquement à VSCODE. Pour cela, il suffit d'ajouter un fichier `tsconfig.json` à la racine de votre module avec le contenu suivant. N'oubliez pas de changer la valeur pour la clé `compilerOptions.baseUrl` avec le chemin absolu vers le dossier `frontend` de votre instance GeoNature.

```json
{
  "compileOnSave": false,
  "compilerOptions": {
    "importHelpers": true,
    "outDir": "../../geonature/frontend/dist/out-tsc",
    "sourceMap": true,
    "declaration": false,
    "module": "es2015",
    "moduleResolution": "node",
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "target": "es5",
    "typeRoots": [
      "node_modules/@types",
      "../../geonature/frontend/node_modules/@types",
      "../../geonature/frontend/src/typings.d.ts"
    ],
    "types": [],
    "lib": ["es2015", "es2016", "es2017", "dom"],
    "baseUrl": "<cheminAbsoluVersVotreGeoNature>/frontend/",
    "paths": {
      "@*": ["node_modules/@*"],
      "@geonature_common/*": [
        "../../geonature/frontend/src/app/GN2CommonModule/*"
      ],
      "@geonature/*": ["../../geonature/frontend/src/app/*"],
      "@geonature_config/*": ["../../geonature/frontend/src/conf/*"],
      "@librairies/*": ["node_modules/*"],
      "tslib": ["node_modules/tslib/tslib.d.ts"]
      //"*": ["node_modules/*"]
    }
  }
}
```

## Installation de votre module

Pour ajouter votre module à votre instance GeoNature, vous pouvez utiliser les commandes suivantes:

```{shell}
source <dossier GeoNature>/backend/venv/bin/activate
geonature install-gn-module <dossier du module> <code du module>
```

**N.B.** Il est possible de faire manuellement l'installation du module. Pour cela, référez-vous à la documentation de GeoNature [#Installation Manuelle](https://docs.geonature.fr/installation.html#installation-manuelle)

Pour que les changements soit pris en compte sur l'instance de GeoNature, redémarrer les services `geonature` et `geonature-worker`.

```{shell}
sudo systemctl restart geonature
sudo systemctl restart geonature-worker
```

## Documentation GeoNature :

Une documentation plus large sur GeoNature contient déjà quelques paragraphes sur la création de module externe :

- Développer un module GeoNature : https://docs.geonature.fr/development.html#developper-un-module-externe
- Installer un module GeoNature : https://docs.geonature.fr/installation.html#installation-d-un-module-geonature
