"""create_template_schema

Revision ID: 06261234b984
Revises: 
Create Date: 2021-03-29 18:38:24.512562

"""
from alembic import op, context
import sqlalchemy as sa
import pkg_resources

from gn_module_template import MODULE_CODE


# revision identifiers, used by Alembic.
revision = '06261234b984'  # CHANGE ME!
down_revision = None
branch_labels = ('template',)
depends_on = None


schema = 'gn_template'


def upgrade():
    op.execute("""
        INSERT INTO gn_commons.t_modules (
            module_code,
            module_label,
            module_path,
            module_target,
            module_picto,
            active_frontend,
            active_backend
        ) VALUES (
            'TEMPLATE',
            'template',
            'template',
            '_self',
            'fa-puzzle-piece',
            TRUE,
            TRUE
        )
    """)
    operations = pkg_resources.resource_string("gn_module_template.migrations", f"data/schema.sql").decode('utf-8')
    op.execute(operations)


def downgrade():
    op.execute(f'DROP TABLE {schema}.my_table')
    op.execute(f'DROP SCHEMA {schema}')
    op.execute(f"DELETE FROM gn_commons.t_modules WHERE module_code = '{MODULE_CODE}'")
