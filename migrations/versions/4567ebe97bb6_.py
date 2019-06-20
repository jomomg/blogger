"""empty message

Revision ID: 4567ebe97bb6
Revises: 5407435d43ab
Create Date: 2019-06-20 15:03:02.254069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4567ebe97bb6'
down_revision = '5407435d43ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.String(length=28), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=180), nullable=True),
    sa.Column('description', sa.String(length=360), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.String(length=28), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.Column('blog_id', sa.String(length=28), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    # ### end Alembic commands ###