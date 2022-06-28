import string
from typing import List, Optional
from pydantic import BaseModel



class Document(BaseModel):
    document_id:str


class SaveDocument(BaseModel):
    document_category_id:str
    user_id:int
    court:str
    state:str
    city:str
    first_name:str
    last_name:str
    religion:str
    gender:str
    address:str
    middle_name:str
    nationality:str
    docNo:str
    docType:str
    issuer:str
    issuerAddress:str
    deponentImage:str
    price:str
    




class ShowSaveDocument(BaseModel):
    document_category_id:str
    id:str
    user_id:int
    court:str
    state:str
    city:str
    first_name:str
    last_name:str
    religion:str
    gender:str
    address:str
    middle_name:str
    nationality:str
    docNo:str
    docType:str
    issuer:str
    issuerAddress:str
    



class PayForDocument(BaseModel):
    transaction_id:str
    user_id:int
    saved_document_id:str
    
    




    
class AttestDocument(BaseModel):
    document_ref:str
    document:str