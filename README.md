# Ansible setup of FastAPI API with database

### Step 1: Run app.yaml
Run the following command to set up the folder:
```bazaar
ansible-playbook app.yaml
```
### Step 2: Configure db with migration folder
Go to the migration folder and run the script:
```bazaar
./db_init.sh
```
This will create the database.

Go to the alembic/versions folder and locate the file that was just created for this migration. Inside the file replace the upgrade and downgrade with:
```bazaar
def upgrade() -> None:
    op.create_table(
        'todos',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('status', sa.Boolean, default=False)
    )


def downgrade() -> None:
    op.drop_table('todos')
```
Then in the import section add the following:
```bazaar
from sqlalchemy.dialects.postgresql import UUID
import uuid
```
Run the following script to run the migration:
```bazaar
./db_migrate.sh
```
Once that is successful run the following script to spin up the server:
```bazaar
./server_start.sh
```
You can curl the server to make sure that everything is working properly:
```bazaar
curl http://localhost:8000/api/v1/todos/
```

### Step 3: Run cleanup.yaml
Run the following command to clean up the folder:
```bazaar
ansible-playbook cleanup.yaml
```
