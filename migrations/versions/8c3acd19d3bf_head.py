"""head

Revision ID: 8c3acd19d3bf
Revises: 62bd7f8e49aa
Create Date: 2024-01-17 23:17:47.448632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c3acd19d3bf'
down_revision: Union[str, None] = '62bd7f8e49aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
