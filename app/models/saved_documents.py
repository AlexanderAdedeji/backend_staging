from pickle import TRUE
from typing import ByteString, Text
from sqlalchemy import Integer, Column, Boolean, String, LargeBinary 
from app.commonLib.models import Base





class SavedDocuments(Base):
    __tablename__ = 'saved_documents'
    id =Column(String, primary_key=True)
    user_id = Column(String,nullable=False)
    document_category= Column(String, nullable=False)
    court= Column(String, nullable=False)
    state= Column(String, nullable=False)
    city= Column(String, nullable=False)
    first_name= Column(String, nullable=True)
    last_name= Column(String, nullable=True)
    religion= Column(String, nullable=True)
    gender= Column(String, nullable=True)
    address= Column(String, nullable=True)
    middle_name= Column(String, nullable=True)
    nationality= Column(String, nullable=True)
    docNo= Column(String, nullable=True)
    qr_code= Column(LargeBinary, nullable=True)
    docType= Column(String, nullable=True)
    issuer= Column(String, nullable=True)
    issuerAddress= Column(String, nullable=True)
    deponentImage=Column(String, nullable=True)
    price=Column(String, nullable=True)

    

    
 
    
