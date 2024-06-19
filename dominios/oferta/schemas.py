from pydantic import BaseModel
from typing import Optional

class Oferta(BaseModel):
    id: Optional[int]= None
    nombre : str
    descripcion : str
    validez: int


