import string
from typing import List, Optional
from pydantic import BaseModel



class Commissioner(BaseModel):
    first_name:str
    last_name:str
    email:str

    
    
    
class CommissionerCreate(Commissioner):
    phone:str
    password:str



class CommissionerLogin(BaseModel):
    email:str
    password:str



class CommissionerValidated(Commissioner):
    id:str
    signature:Optional[str]
    
class UploadSignature(BaseModel):
    id:str
    signature:str
    
