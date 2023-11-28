from flask import current_app
from sqlalchemy import ForeignKey

# import utiles pour déclarer les classes SQLAlchemy
from sqlalchemy.sql import select, func, and_
from sqlalchemy.dialects.postgresql import UUID

from geoalchemy2 import Geometry

# méthode de sérialisation
from utils_flask_sqla.serializers import serializable
from utils_flask_sqla_geo.serializers import geoserializable

# instance de la BDD
from geonature.utils.env import DB


# ajoute la méthode as_dict() à la classe
@serializable
# ajoute la méthode as_geofeature() générant un geojson à la classe
# @geoserializable
class MyModel(DB.Model):
    __tablename__ = "my_table"
    __table_args__ = {"schema": "gn_{{cookiecutter.module_code.lower()}}"}
    pk = DB.Column(DB.Integer, primary_key=True)
