#!/usr/bin/python3

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://fastapi_tutorial:12345@localhost:5432/fastapi', echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)






# psql -U fastapi_tutorial -d "fastapi"