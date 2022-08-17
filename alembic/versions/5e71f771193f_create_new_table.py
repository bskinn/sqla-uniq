"""create new table

Revision ID: 5e71f771193f
Revises: 80ff71d73255
Create Date: 2022-08-17 09:30:48.747489

"""
import sqlalchemy as sqla
from alembic import op


# revision identifiers, used by Alembic.
revision = '5e71f771193f'
down_revision = '80ff71d73255'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("xref", sqla.Column("prim_id", sqla.Integer(), nullable=False),
                    sqla.Column("data", sqla.Unicode(length=100), nullable=False),
                    sqla.PrimaryKeyConstraint("prim_id"),
                    )


def downgrade() -> None:
    op.drop_table("xref")
    
