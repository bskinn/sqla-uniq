r"""*Module to demonstrate possible alembic/sqlalchemy bug.

It seems that alembic is not honoring the naming_convention
when a `constraint_name` value is passed to
batch_op.create_unique_constraint()

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    9 Apr 2022

**Copyright**
    \(c) Brian Skinn 2021-2022

**Source Repository**
    https://github.com/bskinn/ccl-db

**Documentation**
    *pending*

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

from typing import NamedTuple

import sqlalchemy as sqla
from sqlalchemy.orm import registry
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
