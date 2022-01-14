from flask_sqlalchemy import BaseQuery

from geonature.utils.env import db


def MyModelQuery(BaseQuery):
    def filter_by_scope(self):
        return self


class MyModel(db.Model):
    __tablename__ = "my_table"
    __table_args__ = {"schema": "my_schema"}
    query_class = BaseQuery

    id = db.Column(db.Integer, primary_key=True)

    def has_instance_permission(self, scope):
        if scope == 0:
            return False
        return True
