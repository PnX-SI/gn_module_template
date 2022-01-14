from geonature.utils.env import ma

from .models import MyModel


class MyModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MyModel
        include_fk = True
        load_instance = True
