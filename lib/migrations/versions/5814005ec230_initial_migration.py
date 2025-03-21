"""Initial migration

Revision ID: 5814005ec230
Revises: 
Create Date: 2025-03-11 14:23:27.563828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5814005ec230'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('auditions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actor', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('hired', sa.Boolean(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_auditions_role_id_roles')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auditions')
    op.drop_table('roles')
    # ### end Alembic commands ###
