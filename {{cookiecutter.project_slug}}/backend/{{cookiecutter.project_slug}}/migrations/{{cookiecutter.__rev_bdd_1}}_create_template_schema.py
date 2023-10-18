"""create_template_schema

Revision ID: {{cookiecutter.__rev_bdd_1}}
Revises: 
Create Date: 2021-03-29 18:38:24.512562

"""
import importlib

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "{{cookiecutter.__rev_bdd_1}}"  # CHANGE ME!
down_revision = None
branch_labels = ("{{cookiecutter.module_code.lower()}}",)
depends_on = None


schema = "gn_{{cookiecutter.module_code.lower()}}"


def upgrade():
    operations = importlib.resources.read_text(
        "{{cookiecutter.module_package_name}}.migrations.data", "schema.sql"
    )
    op.execute(operations)


def downgrade():
    op.execute(f"DROP TABLE {schema}.my_table")
    op.execute(f"DROP SCHEMA {schema}")
