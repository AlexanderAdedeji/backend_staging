from app.models.commissioner import Commissioner
from sqlalchemy.orm import Session 
from app.commonLib.repositories import Base
from app.models.verifier import Verifier
from app.schemas.user import UserCreate, FullUser
from app.settings.utilities import Utilities
import uuid







class VerifierRepositories(Base[Verifier]):    
    def get_by_email(self, db, *, email):
        user = db.query(Verifier).filter(Verifier.email == email).first()
        return user
    
    def create(self,db,*, verifier:UserCreate):
        verifier_obj = Verifier(
            id=str(uuid.uuid4()),
            first_name= verifier.first_name,
            last_name= verifier.last_name,
            email= verifier.email,
              phone= verifier.phone,
            hashed_password=Utilities.hash_password(verifier.password),

            )
        db.add(verifier_obj)
        db.commit()
        db.refresh(verifier_obj)
        return verifier_obj   



verifier_repo = VerifierRepositories(Verifier)