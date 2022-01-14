import pytest
from flask import url_for
from werkzeug.exceptions import Unauthorized, Forbidden, BadRequest

from geonature.utils.env import db
from geonature.tests.utils import set_logged_user_cookie
from geonature.tests.fixtures import users

from gn_module_template.models import MyModel


@pytest.fixture
def my_models():
    models = []
    with db.session.begin_nested():
        obj = MyModel()
        db.session.add(obj)
        models.append(obj)
    return models


@pytest.mark.usefixtures("client_class", "temporary_transaction")
class TestTemplate:
    def test_list_my_model(self, users):
        response = self.client.get(url_for("gn_module_template.list_my_model"))
        assert response.status_code == Unauthorized.code

        set_logged_user_cookie(self.client, users['noright_user'])
        response = self.client.get(url_for("gn_module_template.list_my_model"))
        assert response.status_code == Forbidden.code

        set_logged_user_cookie(self.client, users['user'])
        response = self.client.get(url_for("gn_module_template.list_my_model"))
        assert response.status_code == 200

    def test_get_my_model(self, users, my_models):
        obj = my_models[0]
        response = self.client.get(url_for("gn_module_template.get_my_model", pk=obj.id))
        assert response.status_code == Unauthorized.code

        set_logged_user_cookie(self.client, users['noright_user'])
        response = self.client.get(url_for("gn_module_template.get_my_model", pk=obj.id))
        assert response.status_code == Forbidden.code

        set_logged_user_cookie(self.client, users['user'])
        response = self.client.get(url_for("gn_module_template.get_my_model", pk=obj.id))
        assert response.status_code == 200

    def test_delete_my_model(self, users, my_models):
        obj = my_models[0]
        response = self.client.delete(url_for("gn_module_template.delete_my_model", pk=obj.id))
        assert response.status_code == Unauthorized.code

        set_logged_user_cookie(self.client, users['noright_user'])
        response = self.client.delete(url_for("gn_module_template.delete_my_model", pk=obj.id))
        assert response.status_code == Forbidden.code

        set_logged_user_cookie(self.client, users['user'])
        response = self.client.delete(url_for("gn_module_template.delete_my_model", pk=obj.id))
        assert response.status_code == 204
        assert MyModel.query.get(obj.id) is None
