from dataclasses import dataclass
from sqlalchemy import create_engine
from app.models.base.base_model import BaseModel

@dataclass
class AppSession:

    __engine = create_engine("postgresql://root:root@localhost/portfolio")

    def create_tables(self):
        try:
            BaseModel.metadata.create_all(self.__engine)
        except Exception as e:
            raise e