"""empty message

Revision ID: b9cb0f88be69
Revises: a28184e99121
Create Date: 2019-06-19 15:22:02.149728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9cb0f88be69'
down_revision = 'a28184e99121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=False),
    sa.Column('date', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.Column('page', sa.Boolean(create_constraint=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('page'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
