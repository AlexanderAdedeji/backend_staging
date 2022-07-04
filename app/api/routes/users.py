from app.api.dependencies.db import get_db
from app.models.users import User
from app.repository.users import user_repo
from app.schemas.user import UserCreate, UserLogin, User,UserValidated
from sqlalchemy.orm import Session
from app.settings.utilities import Utilities
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile


router = APIRouter()



@router.post("/login", response_model=UserValidated)
def Login(login: UserLogin,db: Session = Depends(get_db)):
    user = user_repo.get_by_email(db, email=login.email)
    if not user:
        raise HTTPException(status_code=404, detail=f'Invalid Login Credentials') 
    is_password = Utilities.verify_password(login.password, user.hashed_password)
    if not is_password:
        raise HTTPException(status_code=403,detail= f'Invalid Login Credentials')
    # if not user.is_active:
    #     raise HTTPException(status_code=403,detail= f'Account not active')
    

    return UserValidated(
                id=user.id,
                email = user.email,
                first_name=user.first_name,
                last_name=user.last_name
          

            )
        
        
        
        
@router.post("/sign_up",
             response_model=UserValidated
             )

def signUp(user: UserCreate, db:Session= Depends(get_db)):
     
    user_exist = user_repo.get_by_email(db, email=user.email)
    if user_exist:
        raise HTTPException(status_code=403, detail ='this email already exists')
    
    user = user_repo.create(db, user_in=user)
    # user =  user_repo.get_by_email(db, email=new_user.email)
    return UserValidated(
                id=user.id,
                email = user.email,
                first_name=user.first_name,
                last_name=user.last_name
          

            )
        
    
    
    
    
    
    
@router.post("/update_user",
            #  response_model=User
             )

def signUp(email:str = Form(...), signature: UploadFile = Form(...), db:Session= Depends(get_db)):
     
    # user_exist = user_repo.get_by_email(db, email=user.email)
    # if user_exist:
    #     raise HTTPException(status_code=403, detail ='this email already exists')
    
    # new_user = user_repo.create(db, user_in=user)
    return "hello"
    # return User(
    #     first_name=new_user.first_name,
    #     last_name= new_user.last_name,
    #     email = new_user.email,
    
    #     )
    
    
    
