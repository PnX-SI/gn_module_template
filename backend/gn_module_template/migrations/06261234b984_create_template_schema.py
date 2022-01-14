"""create_template_schema

Revision ID: 06261234b984
Revises: 
Create Date: 2021-03-29 18:38:24.512562

"""
import importlib

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06261234b984'  # CHANGE ME!
down_revision = None
branch_labels = ('template',)
depends_on = None


schema = 'my_schema'


def upgrade():
    op.execute(f"CREATE SCHEMA {schema}")
    op.create_table(
        'my_table',
        sa.Column('id', sa.INTEGER, primary_key=True),
        schema=schema,
    )


def downgrade():
    op.drop_table('my_table', schema=schema)
    op.execute(f"DROP SCHEMA {schema}")
