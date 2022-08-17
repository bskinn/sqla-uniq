"""first test check constraint

Revision ID: bd2de911e129
Revises:
Create Date: 2022-08-16 23:16:03.203789

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "bd2de911e129"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.create_check_constraint(
            constraint_name="positive_value", condition="value > 0"
        )


def downgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.drop_constraint(constraint_name="positive_value", type_="check")
