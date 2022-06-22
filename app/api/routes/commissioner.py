from app.api.dependencies.db import get_db
from app.models.saved_documents import SavedDocuments
from app.models.users import User
from app.repository.commissioner import commissioner_repo
from app.repository.users import user_repo
from app.schemas.commissioner import Commissioner, CommissionerCreate, CommissionerLogin, CommissionerValidated, UploadSignature
from app.schemas.user import UserCreate, UserLogin, User,UserValidated
from sqlalchemy.orm import Session
from app.settings.utilities import Utilities
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()



@router.post("/commissioner_login", response_model=CommissionerValidated)
def Login(login: CommissionerLogin,db: Session = Depends(get_db)):
    commissioner = commissioner_repo.get_by_email(db, email=login.email)
    if not commissioner:
        raise HTTPException(status_code=404, detail=f'Invalid Login Credentials') 
    is_password = Utilities.verify_password(login.password, commissioner.hashed_password)
    if not is_password:
        raise HTTPException(status_code=403,detail= f'Invalid Login Credentials')

    return CommissionerValidated(
                id=commissioner.id,
                email = commissioner.email,
                first_name=commissioner.first_name,
                last_name=commissioner.last_name,
                signature=commissioner.signature
          

            )
        
        
        
        
@router.post("/create_commisioner",
             response_model=Commissioner
             )

def signUp(commissioner: CommissionerCreate, db:Session= Depends(get_db)):
     
    user_exist = commissioner_repo.get_by_email(db, email=commissioner.email)
    if user_exist:
        raise HTTPException(status_code=403, detail ='this email already exists')
    
    new_commissioner = commissioner_repo.create(db, commissioner_in=commissioner)
    return Commissioner(
        first_name=new_commissioner.first_name,
        last_name= new_commissioner.last_name,
        email = new_commissioner.email,
    
        )
    
    
    
    


@router.get("/get_document" )
def signUp(documentRef:str, db:Session= Depends(get_db)):
    document = db.query(SavedDocuments).filter(SavedDocuments.id == documentRef).first()
    if not document:
        raise HTTPException(status_code=404, detail=f'Document Does not exist') 
    
    return document
    
    

    
@router.put("/update_signature", response_model=CommissionerValidated)
def updateSignature(upload_signature:UploadSignature, db:Session=Depends(get_db)):
    commissioner = commissioner_repo.get(db, id=upload_signature.id)
    if not commissioner:
        raise HTTPException(status_code=403, detail ='this Commissioner does not exists')


    commissioner_repo.set_signature(db, db_obj=commissioner,signature=upload_signature.signature)
    return CommissionerValidated(
                        id=commissioner.id,
                email = commissioner.email,
                first_name=commissioner.first_name,
                last_name=commissioner.last_name,
                signature=commissioner.signature
    )