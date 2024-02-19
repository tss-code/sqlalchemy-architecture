from app.models.base_model import BaseModel
from uuid import uuid4
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Company(BaseModel):
    __tablename__ = "companies"
    
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    uuid: Mapped[str] = mapped_column(nullable=False, unique=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    recruiters: Mapped[List["Recruiter"]] = relationship(back_populates="company", cascade="all, delete-orphan")

    @property
    def recruiters_amount(self):
        return len(self.recruiters)
    

class Recruiter(BaseModel):
    __tablename__ = "recruiters"
    
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    uuid: Mapped[str] = mapped_column(nullable=False, unique=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    company_id: Mapped[str] = mapped_column(ForeignKey("companies.uuid"))
    company: Mapped["Company"] = relationship(back_populates="recruiters")