import string
from typing import List, Optional
from pydantic import BaseModel



class Verifier(BaseModel):
    first_name:str
    last_name:str
    email:str

    
    
    
class VerifierCreate(Verifier):
    phone:str
    password:str



class VerifierLogin(BaseModel):
    email:str
    password:str



class VerifierValidated(Verifier):
    id:str
    signature:Optional[str]
    stamp:Optional[str]
    
class UploadSignature(BaseModel):
    id:str
    signature:str


class UploadStamp(BaseModel):
    id:str
    stamp:str
    
