from sqlalchemy import Integer, Column, Boolean, String
from app.commonLib.models import Base





class SavedDocuments(Base):
    __tablename__ = 'saved_documents'
    id =Column(String, primary_key=True)
    user_id = Column(String,nullable=False)
    document_category= Column(String, nullable=False)
    court= Column(String, nullable=False)
    state= Column(String, nullable=False)
    city= Column(String, nullable=False)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    religion= Column(String, nullable=False)
    gender= Column(String, nullable=False)
    address= Column(String, nullable=False)
    middle_name= Column(String, nullable=False)
    nationality= Column(String, nullable=False)
    docNo= Column(String, nullable=False)
    qr_code= Column(String, nullable=False)

    
 
    
