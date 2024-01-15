
from codecs import encode
from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies.db import get_db
import qrcode
from sqlalchemy.orm import Session
import string
import random
import uuid
from io import BytesIO
from app.models.attested_documents import AttestedDocuments
from app.models.paid_documents import PaidDocuments
from app.models.saved_documents import SavedDocuments

from app.schemas.document import  Document, PayForDocument, RetrieveDocument, SaveDocument
from app.settings.utilities import Utilities


router = APIRouter()



# @router.get("/get_document")
# def get_single_document(documentRef:str,db:Session= Depends(get_db)):
#     document = db.query(SavedDocuments).filter(SavedDocuments.document_ref==documentRef).first()
#     if not document:
#         raise HTTPException(status=404, detail=f"Document with id {documentRef} does not exist")
    
#     return document

@router.get("/get_my_documents")
def get_my_documents(id:int,db:Session= Depends(get_db)):
    document = db.query(SavedDocuments).filter(SavedDocuments.user_id==id).first()    
    return document

@router.post("/save_document")
def save_document(document:SaveDocument,db:Session= Depends(get_db)):
    letters = string.ascii_lowercase 
    result1 = ''.join((random.sample(letters, 10)))  
    input_data = f"https://e-affidavit-staging.netlify.app/qr-searchDocument/{result1.upper()}" 
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str= encode(buffered.getvalue(),encoding='base64')
    documentObj = SavedDocuments(id=result1.upper(),user_id=document.user_id, document_category=document.document_category_id, court=document.court,
    state= document.state,
    city=document.city,
    first_name= document.first_name,
    last_name= document.last_name,
    religion= document.religion,
    gender= document.gender,
    address= document.address,
    middle_name=document.middle_name,
    nationality= document.nationality,
    docNo=document.docNo,
    qr_code=img_str,
    docType=document.docType,
    issuer=document.issuer,
    issuerAddress=document.issuerAddress,
    deponentImage=document.deponentImage,
    price=document.price
)
    db.add(documentObj)
    db.commit()
    db.refresh(documentObj)

    return documentObj



@router.post("/pay_for_document")
def pay_for_document(payment_data:PayForDocument,db:Session= Depends(get_db)):

    paymentObj = PaidDocuments(user_id=payment_data.user_id, saved_document_id=payment_data.saved_document_id,payment_ref=payment_data.transaction_id)
    db.add(paymentObj)
    db.commit()
    db.refresh(paymentObj)
    
    document = db.query(SavedDocuments).filter(SavedDocuments.id == paymentObj.saved_document_id).first()
    
    return document




@router.post("/random_ref")
def random_ref(length:int):
    letters = string.ascii_lowercase # define the specific string  
    # define the condition for random.sample() method  
    
    input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"
    result1 = ''.join((random.sample(letters, length)))   

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(result1.upper())
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = Utilities.convert_to_base_64(buffered.getvalue())
    img.save('qrcode001.jpeg')
    # base_64 =Utilities.convert_to_base_64(img)
    

    return img_str






@router.post("/get_document_in_qr")
def get_document_in_qr(documentRef:str, db:Session =Depends(get_db)): 
    document = db.query(AttestedDocuments).filter(AttestedDocuments.document_ref==documentRef).first()
    if not document:
        document = db.query(SavedDocuments).filter(SavedDocuments.id == documentRef).first()
        if not document:
            raise HTTPException(status_code=404, detail=f'Document Does not exist') 
    
    return document

@router.get("/get_documents_saved_by_user")
def get_documents_saved_by_user(user_id:str, db:Session =Depends(get_db)):
    new_array=[]
    saved_documents =db.query(SavedDocuments.id,SavedDocuments.document_category, SavedDocuments.CreatedAt).filter(SavedDocuments.user_id == user_id).all()
    for document in saved_documents:
        paid = db.query(PaidDocuments.saved_document_id).filter(document.id == PaidDocuments.saved_document_id).all()
        attested = db.query(AttestedDocuments.document_ref).filter(document.id == AttestedDocuments.document_ref).all()

        if not attested:
            if not paid:     
                new_document = RetrieveDocument(status='Saved', document_category=document.document_category, id=document.id, created_at= document.CreatedAt)
                new_array.append(new_document)
            else:
                new_document = RetrieveDocument(status='Paid', document_category=document.document_category, id=document.id, created_at= document.CreatedAt)
                new_array.append(new_document)
        else:
             new_document = RetrieveDocument(status='Attested', document_category=document.document_category, id=document.id, created_at= document.CreatedAt)
             new_array.append(new_document)

    return new_array