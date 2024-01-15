from fastapi import APIRouter
from app.api.routes import documents
from app.api.routes import users
from app.api.routes import commissioner
from app.api.routes import verifier




router =APIRouter()

router.include_router(users.router, tags=["Users"], prefix="/user")
router.include_router(documents.router, tags=["Documents"], prefix="/documents")
router.include_router(commissioner.router, tags=["Commissioner"], prefix="/commissioner")
router.include_router(verifier.router, tags=["Verifier"], prefix="/verifier")