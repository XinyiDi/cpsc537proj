"""empty message

Revision ID: dc4faa94ecce
Revises: bdb6d37e2325
Create Date: 2023-11-20 21:22:38.184694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc4faa94ecce'
down_revision = 'bdb6d37e2325'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('artists', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_timestamp')

    op.drop_table('post')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plan', sa.String(length=120), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=120),
               existing_nullable=True)
        batch_op.drop_index('ix_user_email')
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(batch_op.f('ix_user_plan'), ['plan'], unique=True)
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_plan'))
        batch_op.create_index('ix_user_username', ['username'], unique=False)
        batch_op.create_index('ix_user_email', ['email'], unique=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.alter_column('id',
               existing_type=sa.String(length=120),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('plan')

    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index('ix_post_timestamp', ['timestamp'], unique=False)

    op.drop_table('songs')
    op.drop_table('artists')
    # ### end Alembic commands ###