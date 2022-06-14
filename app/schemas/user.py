import string
from typing import List, Optional
from pydantic import BaseModel



class User(BaseModel):
    first_name:str
    last_name:str
    email:str


class FullUser(User):
    is_active:str
    photo:str
    signature:str
    address:str
    

class UserCreate(User):
    password:str
    


class UserLogin(BaseModel):
    email:str
    password:str

    
class UserValidated(User):
    id:int

    
    
class DisplayUser(User):
    id:int
    is_active:bool