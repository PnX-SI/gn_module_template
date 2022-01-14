from flask import Blueprint, current_app
from werkzeug.exceptions import Forbidden

from geonature.core.gn_permissions.decorators import check_cruved_scope
from geonature.core.gn_permissions.tools import get_scopes_by_action
from geonature.utils.env import db

from .models import MyModel
from .schemas import MyModelSchema


blueprint = Blueprint('gn_module_template', __name__)


@blueprint.route('/my_models/', methods=['GET'])
@check_cruved_scope('R', module_code='TEMPLATE', get_scope=True)
def list_my_model(scope):
    obj = MyModel.query.all()#filter_by_scope(scope).all()
    obj_schema = MyModelSchema()
    return obj_schema.jsonify(obj, many=True)


@blueprint.route('/my_models/<int:pk>', methods=['GET'])
@check_cruved_scope('R', module_code='TEMPLATE', get_scope=True)
def get_my_model(scope, pk):
    obj = MyModel.query.get_or_404(pk)
    if not obj.has_instance_permission(scope):
        raise Forbidden
    obj_schema = MyModelSchema()
    return obj_schema.jsonify(obj)


@blueprint.route('/my_models/', methods=['POST'])
@check_cruved_scope('C', module_code='TEMPLATE')
def create_my_model():
    obj_schema = MyModelSchema()
    obj = obj_schema.load(obj_schema)
    db.session.add(obj)
    db.session.commit()
    return obj_schema.jsonify(obj)


@blueprint.route('/my_models/<int:pk>', methods=['PATCH'])
@check_cruved_scope('U', module_code='TEMPLATE', get_scope=True)
def update_my_model(scope, pk):
    obj = MyModel.query.get_or_404(pk)
    if not obj.has_instance_permission(scope):
        raise Forbidden
    obj_schema = MyModelSchema()
    obj_schema.load(request.params, instance=obj)
    db.session.commit()
    return obj_schema.jsonify(obj)


@blueprint.route('/my_models/<int:pk>', methods=['DELETE'])
@check_cruved_scope('D', module_code='TEMPLATE', get_scope=True)
def delete_my_model(scope, pk):
    obj = MyModel.query.get_or_404(pk)
    if not obj.has_instance_permission(scope):
        raise Forbidden
    db.session.delete(obj)
    db.session.commit()
    return '', 204
