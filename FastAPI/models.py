from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    description = Column(String, index=True)
    amount = Column(Float, index=True)
    category = Column(String, index=True)
    is_income = Column(Boolean, default=False)
    
    