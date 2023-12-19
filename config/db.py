from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="dqdusvpgg",
    api_key="342297133418356",
    api_secret="Pg3zEL3tg_cZ_10s5o5eaxFutSw"
)

DATABASE_URL = "postgresql://postgres:Mano@127.0.0.1:5432/recruitment"

# DATABASE_URL = "postgresql://loan_approval_user:pbnpeLikiGqrPcoHRLZMa6EJn7aNGWLy@dpg-clu0qnol5elc7387ostg-a.oregon-postgres.render.com/loan_approval"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()