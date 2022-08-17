"""add fkey to foo

Revision ID: 1cad7a962ed8
Revises: 5e71f771193f
Create Date: 2022-08-17 09:35:15.592769

"""
import sqlalchemy as sqla
from alembic import op



# revision identifiers, used by Alembic.
revision = '1cad7a962ed8'
down_revision = '5e71f771193f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.add_column(sqla.Column("xref_id", sqla.Integer))
        batch_op.create_foreign_key(constraint_name=None,
                                    referent_table="xref",
                                    local_cols=["xref_id"],
                                    remote_cols=["prim_id"])


def downgrade() -> None:
    with op.batch_alter_table("foo") as batch_op:
        batch_op.drop_constraint(constraint_name="fk_foo_xref_id_xref", type_="foreignkey")
        batch_op.drop_column("xref_id")
