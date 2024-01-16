from app.api.dependencies.db import get_db
from app.models.attested_documents import AttestedDocuments
from app.models.saved_documents import SavedDocuments
from app.models.users import User
from app.repository.commissioner import commissioner_repo
from app.repository.users import user_repo
from app.schemas.commissioner import Commissioner, CommissionerCreate, CommissionerLogin, CommissionerValidated, UploadSignature, UploadStamp
from app.schemas.document import AttestDocument
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
                signature=commissioner.signature,
                stamp=commissioner.stamp
          

            )
        
        
        
        
@router.post("/create_commissioner",
             response_model=CommissionerValidated
             )

def signUp(commissioner: CommissionerCreate, db:Session= Depends(get_db)):
     
    user_exist = commissioner_repo.get_by_email(db, email=commissioner.email)
    if user_exist:
        raise HTTPException(status_code=403, detail ='this email already exists')
    
    new_commissioner =commissioner_repo.create(db, commissioner_in=commissioner)
    return CommissionerValidated(
                id=new_commissioner.id,
                email = new_commissioner.email,
                first_name=new_commissioner.first_name,
                last_name=new_commissioner.last_name,
                signature=new_commissioner.signature
          

            )
    
    
    
    


@router.get("/get_document" )
def get_document(documentRef:str, db:Session= Depends(get_db)):
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



@router.put("/update_stamp", response_model=CommissionerValidated)
def updateSignature(upload_stamp:UploadStamp, db:Session=Depends(get_db)):
    commissioner = commissioner_repo.get(db, id=upload_stamp.id)
    if not commissioner:
        raise HTTPException(status_code=403, detail ='this Commissioner does not exists')


    commissioner_repo.set_stamp(db, db_obj=commissioner,stamp=upload_stamp.stamp)
    return CommissionerValidated(
                        id=commissioner.id,
                email = commissioner.email,
                first_name=commissioner.first_name,
                last_name=commissioner.last_name,
                signature=commissioner.signature,
                stamp=commissioner.stamp
    )



@router.post('/attest_document')
def attest_document(doc:AttestDocument, db:Session =Depends(get_db)):
    documentToAttest = AttestedDocuments(**doc.dict())
    db.add(documentToAttest)
    db.commit()
    db.refresh(documentToAttest)
    return documentToAttest