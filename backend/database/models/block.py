from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True)
    index = Column(Integer, unique=True, nullable=False)
    previous_hash = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    nonce = Column(Integer, nullable=False)
    hash = Column(String, nullable=False)
    transactions = Column(String, nullable=False)  # Transactions as JSON string or list of tx IDs
