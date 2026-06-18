from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.settings import (

    POSTGRES_HOST,

    POSTGRES_DB,

    POSTGRES_USER,

    POSTGRES_PASSWORD
)

DATABASE_URL = (

    f"postgresql://"

    f"{POSTGRES_USER}:"

    f"{POSTGRES_PASSWORD}@"

    f"{POSTGRES_HOST}:5432/"

    f"{POSTGRES_DB}"
)

engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True
)

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine
)

Base = declarative_base()