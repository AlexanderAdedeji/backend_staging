from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings.configurations.config import Settings




settings =Settings()

# uri = settings.DATABASE_URL
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)

# if settings.DEBUG == True:
#     SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# else:
#     SQLALCHEMY_DATABASE_URL = uri

    
# SQLALCHEMY_DATABASE_URL = "postgresql://ozswcniofjwjez:70e98db7574cc95162050138b56dbd6e4db6c562072c2a5f4647943280ab4d05@ec2-54-157-16-196.compute-1.amazonaws.com:5432/dc60igb8j3grgv"

SQLALCHEMY_DATABASE_URL = (
    #  "sqlite:///./sql_app.db"
    f"postgresql+psycopg2://"
    f"identikoPostgresSqlDevAdmin@identiko-postgres-dev-server:"
    f"Cheaters2026.@"
    f"identiko-postgres-dev-server.postgres.database.azure.com:"
    f"5432/StagingEAffidavit"
)



engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()