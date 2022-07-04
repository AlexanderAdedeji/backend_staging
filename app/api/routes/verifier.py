
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies.db import get_db
from app.models.attested_documents import AttestedDocuments
from app.repository.verifier import verifier_repo
from app.schemas.verifier import Verifier, VerifierCreate, VerifierLogin, VerifierValidated
from app.settings.utilities import Utilities


router = APIRouter()

@router.post("/verifier_login", response_model=VerifierValidated)
def Login(login: VerifierLogin,db: Session = Depends(get_db)):
    verifier = verifier_repo.get_by_email(db, email=login.email)
    if not verifier:
        raise HTTPException(status_code=404, detail=f'Invalid Login Credentials') 
    is_password = Utilities.verify_password(login.password, verifier.hashed_password)
    if not is_password:
        raise HTTPException(status_code=403, detail= f'Invalid Login Credentials')

    return VerifierValidated(
                id=verifier.id,
                email = verifier.email,
                first_name=verifier.first_name,
                last_name=verifier.last_name,
                signature=verifier.signature
          

            )
        


@router.post("/create_verifier",
             response_model=Verifier
             )

def signUp(verifier: VerifierCreate, db:Session= Depends(get_db)):
     
    user_exist = verifier_repo.get_by_email(db, email=verifier.email)
    if user_exist:
        raise HTTPException(status_code=403, detail ='this email already exists')
    
    new_Verifier = verifier_repo.create(db, verifier=verifier)
    return Verifier(
        first_name=new_Verifier.first_name,
        last_name= new_Verifier.last_name,
        email = new_Verifier.email,
    
        )

@router.get("/get_attested_document")
def get_attested_doc(documentRef:str,db:Session =Depends(get_db)):
    document = db.query(AttestedDocuments).filter(AttestedDocuments.document_ref==documentRef).first()
    if not document:
        raise HTTPException(status=404, detail=f"Document with id {documentRef} does not exist")
    return document