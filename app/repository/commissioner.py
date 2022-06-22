from app.models.commissioner import Commissioner
from sqlalchemy.orm import Session 
from app.commonLib.repositories import Base
from app.schemas.user import UserCreate, FullUser
from app.settings.utilities import Utilities
import uuid







class CommissionerRepositories(Base[Commissioner]):    
    def get_by_email(self, db, *, email):
        user = db.query(Commissioner).filter(Commissioner.email == email).first()
        return user
    
    def create(self,db,*, commissioner_in:UserCreate):
        commissioner_obj = Commissioner(
            id=str(uuid.uuid4()),
            first_name= commissioner_in.first_name,
            last_name= commissioner_in.last_name,
            email= commissioner_in.email,
              phone= commissioner_in.phone,
            hashed_password=Utilities.hash_password(commissioner_in.password),

            )
        db.add(commissioner_obj)
        db.commit()
        db.refresh(commissioner_obj)
        return commissioner_obj
    
    def set_activation_status(self, db: Session,*, db_obj: Commissioner, status:bool):
        return super().update(db, db_obj=db_obj, obj_in={"is_active": status})
    def set_signature(self, db: Session,*, db_obj: Commissioner, signature:str):
            return super().update(db, db_obj=db_obj, obj_in={"signature": signature})
    
    def activate(self,db: Session, *, db_obj:Commissioner):
        return self.set_activation_status(db=db, db_obj=db_obj, status=True)
    
    
    def deactivate(self,db: Session,*, db_obj: Commissioner):
        return self.set_activation_status(db=db, db_obj=db_obj, status=False)

    



commissioner_repo = CommissionerRepositories(Commissioner)