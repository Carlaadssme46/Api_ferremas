from sqlalchemy import Column, Integer, String
from ...database import Base

class Sucursal(Base):
    __tablename__='sucursal'
    id=Column(Integer,primary_key=True)
    nombre=Column(String)
    direccion=Column(String)
    telefono=Column(String)
    email = Column(String)