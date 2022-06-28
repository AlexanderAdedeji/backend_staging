from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies.db import get_db
from app.models.attested_documents import AttestedDocuments


router = APIRouter()


@router.get("/login")
def Login():
    return "verifier"


@router.get("/get_attested_document")
def get_attested_doc(documentRef:str,db:Session =Depends(get_db)):
    document = db.query(AttestedDocuments).filter(AttestedDocuments.document_ref==documentRef).first()
    if not document:
        raise HTTPException(status=404, detail=f"Document with id {documentRef} does not exist")
    return document