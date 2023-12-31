from app.models.users import User
from sqlalchemy.orm import Session 
from app.commonLib.repositories import Base
from app.schemas.user import UserCreate, FullUser
from app.settings.utilities import Utilities







class UserRepositories(Base[User]):    
    def get_by_email(self, db, *, email):
        user = db.query(User).filter(User.email == email).first()
        return user
    
    def create(self,db,*, user_in:UserCreate):
        user_obj = User(
            first_name= user_in.first_name,
            last_name= user_in.last_name,
            email= user_in.email,
            hashed_password=Utilities.hash_password(user_in.password),

            )
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj
    
    def set_activation_status(self, db: Session,*, db_obj: User, status:bool):
        return super().update(db, db_obj=db_obj, obj_in={"is_active": status})
    
    def activate(self,db: Session, *, db_obj:User):
        return self.set_activation_status(db=db, db_obj=db_obj, status=True)
    
    
    def deactivate(self,db: Session,*, db_obj: User):
        return self.set_activation_status(db=db, db_obj=db_obj, status=False)

    



user_repo = UserRepositories(User)