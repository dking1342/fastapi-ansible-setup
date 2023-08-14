from sqlalchemy.dialects.postgresql import UUID
import uuid


def upgrade() -> None:
    op.create_table(
        'todos',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('status', sa.Boolean, default=False)
    )


def downgrade() -> None:
    op.drop_table('todos')