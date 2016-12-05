"""empty message

Revision ID: 085a86f1604e
Revises: 8f9d7bd53596
Create Date: 2016-12-05 15:46:34.523513

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '085a86f1604e'
down_revision = '8f9d7bd53596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_dex', sa.Integer(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('forme', sa.String(), nullable=True),
    sa.Column('type1', sa.String(), nullable=True),
    sa.Column('type2', sa.String(), nullable=True),
    sa.Column('ability1', sa.String(), nullable=True),
    sa.Column('ability2', sa.String(), nullable=True),
    sa.Column('abilityH', sa.String(), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.Column('defense', sa.Integer(), nullable=True),
    sa.Column('spattack', sa.Integer(), nullable=True),
    sa.Column('spdefense', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('weight', sa.String(), nullable=True),
    sa.Column('height', sa.String(), nullable=True),
    sa.Column('dex1', sa.String(), nullable=True),
    sa.Column('dex2', sa.String(), nullable=True),
    sa.Column('pkmn_class', sa.String(), nullable=True),
    sa.Column('percent_male', sa.Float(), nullable=True),
    sa.Column('percent_female', sa.Float(), nullable=True),
    sa.Column('pre_evolution', sa.String(), nullable=True),
    sa.Column('egg_group1', sa.String(), nullable=True),
    sa.Column('egg_group2', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pokemonTeamBuilderTest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemonTeamBuilderTest',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u'nextval(\'"pokemonTeamBuilderTest_id_seq"\'::regclass)'), nullable=False),
    sa.Column('num_dex', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('species', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('forme', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type1', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ability1', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ability2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('abilityH', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hp', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('attack', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('defense', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('spattack', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('spdefense', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('speed', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('weight', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('height', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('dex1', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('dex2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pkmn_class', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('percent_male', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('percent_female', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pre_evolution', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('egg_group1', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('egg_group2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'pokemonTeamBuilderTest_pkey')
    )
    op.drop_table('pokemon')
    # ### end Alembic commands ###
