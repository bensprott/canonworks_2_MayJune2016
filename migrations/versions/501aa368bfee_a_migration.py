"""a migration

Revision ID: 501aa368bfee
Revises: 3af5f49bfd9
Create Date: 2016-03-26 16:17:12.285000

"""

# revision identifiers, used by Alembic.
revision = '501aa368bfee'
down_revision = '3af5f49bfd9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_of_birth', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_of_birth')
    ### end Alembic commands ###
