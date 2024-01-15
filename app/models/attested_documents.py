from sqlalchemy import Integer, Column, Boolean, String,LargeBinary
from app.commonLib.models import Base






class AttestedDocuments(Base):
    __tablename__="attested_documents"
    id=Column(Integer, primary_key=True, nullable=False)
    document_ref=Column(String, nullable=False)
    document=Column(String,nullable=False)

















