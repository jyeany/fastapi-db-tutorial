"""create users table

Revision ID: 1f04f77486bc
Revises: 
Create Date: 2021-09-26 13:30:38.775080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f04f77486bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), index=True),
        sa.Column('hashed_password', sa.String(100)),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table('users')
