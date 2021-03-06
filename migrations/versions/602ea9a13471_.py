"""empty message

Revision ID: 602ea9a13471
Revises: 496b9489211e
Create Date: 2021-03-29 22:04:14.702707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602ea9a13471'
down_revision = '496b9489211e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.Text(), nullable=True))
        batch_op.alter_column('image_file',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
