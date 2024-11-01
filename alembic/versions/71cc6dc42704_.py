"""empty message

Revision ID: 71cc6dc42704
Revises: 3e8b4789fe64
Create Date: 2024-11-01 17:49:45.254593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71cc6dc42704'
down_revision = '3e8b4789fe64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'is_admin')
    # ### end Alembic commands ###
