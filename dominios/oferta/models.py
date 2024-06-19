from sqlalchemy import Column,Integer,String
from ...database import Base

class Oferta(Base):
    __tablename__='oferta'
    id=Column(Integer,primary_key=True)
    nombre=Column(String)
    descripcion=Column(String)
    validez=Column(Integer)
    