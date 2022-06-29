from fastapi import FastAPI
from app.api.routes.routes import router as global_router
from starlette.middleware.cors import CORSMiddleware
import starlette.responses as _responses
from app.models import users, paid_documents, saved_documents, commissioner, attested_documents, verifier



from app.database.session import SessionLocal, engine
from app.models.verifier import Verifier


paid_documents.Base.metadata.create_all(bind=engine)
saved_documents.Base.metadata.create_all(bind=engine)
users.Base.metadata.create_all(bind=engine)
commissioner.Base.metadata.create_all(bind=engine)
attested_documents.Base.metadata.create_all(bind=engine)
verifier.Base.metadata.create_all(bind=engine)



app = FastAPI()



def create_appication_instance()-> FastAPI:
    application = FastAPI(title="E- Affidavit", debug=True)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(global_router)
    
    return application


app = create_appication_instance()



@app.get('/')
async def root():
    return _responses.RedirectResponse("/docs")