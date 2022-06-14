import string
from typing import List, Optional
from pydantic import BaseModel



class Document(BaseModel):
    document_id:str


class SaveDocument(BaseModel):
    document_category_id:int
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
    




class ShowSaveDocument(BaseModel):
    document_category_id:int
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
    



class PayForDocument(BaseModel):
    transaction_id:str
    user_id:int
    saved_document_id:str
    
    




    
