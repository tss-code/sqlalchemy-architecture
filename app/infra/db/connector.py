from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models.base_model import BaseModel
from app.settings import CONFIG

@dataclass
class AppSession:

    __engine = create_engine(f"postgresql://{CONFIG['POSTGRES_USER']}:{CONFIG['POSTGRES_PASSWORD']}@localhost/{CONFIG['POSTGRES_DB']}")

    def create_tables(self):
        try:
            BaseModel.metadata.create_all(self.__engine)
        except Exception as e:
            raise e

    def add(self, value):
        with Session(self.__engine) as session:
            try:
                if isinstance(value, list):
                    session.add_all(value)
                    return

                session.add(value)
                session.commit()
                session.close()
            except Exception as e:
                raise e
                
