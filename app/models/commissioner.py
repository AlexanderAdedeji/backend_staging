from sqlalchemy import Integer, Column, Boolean, String,LargeBinary
from app.commonLib.models import Base




class Commissioner(Base):
    __tablename__ = 'commissioner'
    id =Column(String, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name=Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone= Column(String, nullable=False)
    hashed_password=Column(String, nullable=False)
    signature=Column(String, nullable=True)
    stamp=Column(String, nullable=True)
    
