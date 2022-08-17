"""add unique constraint

Revision ID: 80ff71d73255
Revises: bd2de911e129
Create Date: 2022-08-16 23:20:40.638063

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "80ff71d73255"
down_revision = "bd2de911e129"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.create_unique_constraint(constraint_name=None, columns=["value"])


def downgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.drop_constraint(constraint_name="value", type_="unique")
