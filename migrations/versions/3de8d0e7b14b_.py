"""empty message

Revision ID: 3de8d0e7b14b
Revises: c3e56903a394
Create Date: 2022-02-23 18:38:48.834207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de8d0e7b14b'
down_revision = 'c3e56903a394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procedure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animal', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('type', sa.Enum('vaccination', 'treatment', name='procedureenum'), nullable=True),
    sa.Column('drug', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['animal'], ['animal.animal_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('procedure')
    # ### end Alembic commands ###
