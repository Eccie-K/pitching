"""Initial Migration

Revision ID: 6c10cc804727
Revises: fbb37c807e73
Create Date: 2019-07-02 12:53:05.373841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c10cc804727'
down_revision = 'fbb37c807e73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('pitch', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('downvotes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('pitch_content', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('upvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'upvotes')
    op.drop_column('pitches', 'pitch_content')
    op.drop_column('pitches', 'downvotes')
    op.drop_table('comments')
    # ### end Alembic commands ###
