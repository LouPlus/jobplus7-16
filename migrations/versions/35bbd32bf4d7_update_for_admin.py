"""update for admin

Revision ID: 35bbd32bf4d7
Revises: f9ff0289db94
Create Date: 2018-08-01 13:54:59.745977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35bbd32bf4d7'
down_revision = 'f9ff0289db94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delivery', sa.Column('company_id', sa.Integer(), nullable=True))
    op.add_column('job', sa.Column('is_disable', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'is_disable')
    op.drop_column('delivery', 'company_id')
    # ### end Alembic commands ###
