from flask import Blueprint

from utils_flask_sqla.response import json_resp
from geonature.utils.env import DB

# import des fonctions utiles depuis le sous-module d'authentification
from geonature.core.gn_permissions import decorators as permissions
from geonature.core.gn_permissions.tools import _get_user_permissions
from .models import MyModel

blueprint = Blueprint(
    "{{cookiecutter.__module_api_prefix}}", __name__
)  # blueprint prefix should be different from existing ones in GeoNature !


# Exemple d'une route simple
@blueprint.route("/test", methods=["GET"])
@json_resp
def get_view():
    q = DB.session.query(MyModel)
    data = q.all()
    return [d.as_dict() for d in data]


# Exemple d'une route protégée le CRUVED du sous module d'authentification
@blueprint.route("/test_cruved", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="{{cookiecutter.module_code}}")
@json_resp
def get_sensitive_view(info_role):
    # Récupérer l'id de l'utilisateur qui demande la route
    id_role = info_role.id_role
    # Récupérer la portée autorisée à l'utilisateur pour l'acton 'R' (read)
    read_scope = info_role.value_filter

    # récupérer le CRUVED complet de l'utilisateur courant
    user_cruved = _get_user_permissions(id_role=info_role.id_role)
    q = DB.session.query(MyModel)
    data = q.all()
    return [d.as_dict() for d in data]
