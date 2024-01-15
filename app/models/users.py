from sqlalchemy import Integer, Column, Boolean, String
from app.commonLib.models import Base




class User(Base):
    __tablename__ = 'Users'
    id =Column(Integer, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name= Column(String, nullable=False)
    middle_name=Column(String, nullable=True)
    email = Column(String, nullable=False)
    photo=Column(String, nullable=True)
    signature=Column(String, nullable=True)
    address= Column(String, nullable=True)
    phone_number=Column(String, nullable=True)
    is_active=Column(Boolean, nullable=False, default=False)
    hashed_password=Column(String, nullable=False)
    
