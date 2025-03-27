from backend.database import engine
from backend.database.models.user import Base as UserBase
from backend.database.models.transaction import Base as TransactionBase
from backend.database.models.block import Base as BlockBase

# Tambahkan nanti: TransactionBase, BlockBase

def create_tables():
    UserBase.metadata.create_all(bind=engine)
    TransactionBase.metadata.create_all(bind=engine)
    BlockBase.metadata.create_all(bind=engine)  # Tambahkan ini untuk Block
    print("✅ User, Transaction, and Block tables created.")

if __name__ == "__main__":
    create_tables()
