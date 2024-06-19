from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencias import get_db
from ..database import SessionLocal
from ..dominios.sucursal import models, schemas
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

routerSucursal=APIRouter(
    tags=["Sucursales"],
    prefix="/sucursales"
)

@routerSucursal.get('/')
async def get_sucursales(db: Session=Depends(get_db)):
    db= SessionLocal()
    data=db.query(models.Sucursal).all()
    return data

@routerSucursal.get('/{id}')
async def get_sucursales(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Sucursal).filter(models.Sucursal.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'sucursal no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))



@routerSucursal.post('/')
async def create_sucursal(sucursal: schemas.Sucursal , db: Session=Depends(get_db)):
    db= SessionLocal()
    nueva_sucursal= models.Sucursal(**sucursal.model_dump())
    db.add(nueva_sucursal)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha creado una sucursal','sucursal': sucursal.model_dump()})


@routerSucursal.put('/{id}')
async def update_suscusal(id:int, sucursal:schemas.Sucursal, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Sucursal).filter(models.Sucursal.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró la sucursal'})
    
    data.nombre = sucursal.nombre
    data.direccion = sucursal.direccion
    data.telefono= sucursal.telefono
    data.email= sucursal.email
    db.commit()
    return JSONResponse(status_code=200, content={'message':'se modificó la sucursal'})

@routerSucursal.delete('/{id}')
async def delete_sucursal(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Sucursal).filter(models.Sucursal.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró la sucursal'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message':'se ha eliminado una sucursal','sucursal':jsonable_encoder(data)})