"""Init

Revision ID: 9bbc128c2927
Revises: 
Create Date: 2024-04-11 09:19:11.268829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bbc128c2927'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(length=25), nullable=True),
    sa.Column('born_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_contacts_id'), 'contacts', ['id'], unique=False)
    op.create_index(op.f('ix_contacts_last_name'), 'contacts', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_last_name'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_id'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###