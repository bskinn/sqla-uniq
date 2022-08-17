r"""*Module to demonstrate possible alembic/sqlalchemy bug.

It seems that alembic is not honoring the naming_convention
when a `constraint_name` value is passed to
batch_op.create_unique_constraint()

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    16 Aug 2022

**Copyright**
    \(c) Brian Skinn 2022

**Source Repository**
    https://github.com/bskinn/sqla-uniq

**License**
    The MIT License; see LICENSE.txt for full license terms

**Members**

"""

import os
from pathlib import Path

import sqlalchemy as sqla
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta


metadata_obj = sqla.schema.MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

reg = registry(metadata=metadata_obj)


class SQLABase(metaclass=DeclarativeMeta):
    """Declarative abstract base class for models."""

    __abstract__ = True

    registry = reg
    metadata = reg.metadata

    __init__ = reg.constructor


del reg


class FooModel(SQLABase):
    """Sqlalchemy model to demonstrate migration misbehavior."""

    __tablename__ = "foo"
    __table_args__ = (sqla.PrimaryKeyConstraint("prim_id"),)

    prim_id = sqla.Column(sqla.Integer)
    value = sqla.Column(sqla.Integer)

    def __repr__(self):
        return f"FooModel(value='{self.value}')"


def create_session(db_path, /, *, create_tables=False):
    db_path = Path(db_path)
    path_str = os.fsdecode(db_path.resolve())
    conn_str = f"sqlite:///{path_str}"
    engine = sqla.create_engine(conn_str, future=True)

    if create_tables:
        SQLABase.metadata.create_all(engine)

    return engine, sessionmaker()(bind=engine)
