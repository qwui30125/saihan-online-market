"""

Revision ID: 04b66376f066
Revises: f1fa8bef0a34
Create Date: 2019-01-18 16:46:42.676843

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04b66376f066'
down_revision = 'f1fa8bef0a34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('seller_id', sa.Integer(), nullable=False))
    op.drop_constraint(u'products_ibfk_1', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'user_profile', ['seller_id'], ['user_id'])
    op.drop_column('products', 'seller')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('seller', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key(u'products_ibfk_1', 'products', 'user_profile', ['seller'], ['user_id'])
    op.drop_column('products', 'seller_id')
    # ### end Alembic commands ###
