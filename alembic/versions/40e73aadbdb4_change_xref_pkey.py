"""Change xref pkey

Revision ID: 40e73aadbdb4
Revises: 1cad7a962ed8
Create Date: 2022-08-17 09:42:53.019146

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '40e73aadbdb4'
down_revision = '1cad7a962ed8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("xref") as batch_op:
        batch_op.drop_constraint(None, type_="primary")
        batch_op.create_primary_key(None, ["data"])


def downgrade() -> None:
    with op.batch_alter_table("xref") as batch_op:
        batch_op.drop_constraint(None, type_="primary")
        batch_op.create_primary_key(None, ["prim_id"])
