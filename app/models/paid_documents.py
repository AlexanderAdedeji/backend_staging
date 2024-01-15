from sqlalchemy import Integer, Column, Boolean, String
from app.commonLib.models import Base





class PaidDocuments(Base):
    __tablename__ = 'paid_documents'
    id =Column(Integer, primary_key=True, index=True)
    user_id = Column(String,nullable=False)
    saved_document_id= Column(String, nullable=False)  
    payment_ref=Column(String, nullable=True)
    
 
    
