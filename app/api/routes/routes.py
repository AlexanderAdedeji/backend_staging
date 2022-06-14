from fastapi import APIRouter
from app.api.routes import documents
from app.api.routes import users
from app.api.routes import commissioner




router =APIRouter()

router.include_router(users.router, tags=["Users"], prefix="/user")
router.include_router(documents.router, tags=["Documents"], prefix="/documents")
router.include_router(commissioner.router, tags=["Commissioner"], prefix="/commissioner")