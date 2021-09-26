"""Add items table

Revision ID: 35e81270f693
Revises: 1f04f77486bc
Create Date: 2021-09-26 13:56:24.694862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35e81270f693'
down_revision = '1f04f77486bc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(100), index=True),
        sa.Column('description', sa.String(500), index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("users.id"))
    )
    # op.create_foreign_key("fk_user_item", "items", "users", ["item_id"], ["id"])


def downgrade():
    op.drop_table('items')
