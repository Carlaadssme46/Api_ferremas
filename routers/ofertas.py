from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencias import get_db
from ..database import SessionLocal
from ..dominios.oferta import models, schemas
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

routerOferta=APIRouter(
    tags=["Ofertas"],
    prefix="/ofertas"
)

@routerOferta.get('/')
async def get_ofertas(db: Session=Depends(get_db)):
    db= SessionLocal()
    data=db.query(models.Oferta).all()
    return data

@routerOferta.get('/{id}')
async def get_ofertas(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Oferta).filter(models.Oferta.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'oferta no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))



@routerOferta.post('/')
async def create_oferta(oferta: schemas.Oferta , db: Session=Depends(get_db)):
    db= SessionLocal()
    nueva_oferta= models.Oferta(**oferta.model_dump())
    db.add(nueva_oferta)
    db.commit()
    return JSONResponse(status_code=201, content={'message':'Se ha creado una oferta','oferta': oferta.model_dump()})


@routerOferta.put('/{id}')
async def update_oferta(id:int, oferta:schemas.Oferta, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Oferta).filter(models.Oferta.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró la oferta'})
    
    data.nombre = oferta.nombre
    data.descripcion = oferta.descripcion
    data.validez= oferta.validez
    db.commit()
    return JSONResponse(status_code=200, content={'message':'se modificó la oferta'})

@routerOferta.delete('/{id}')
async def delete_oferta(id:int, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Oferta).filter(models.Oferta.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'no se encontró la oferta'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message':'se ha eliminado una oferta','oferta':jsonable_encoder(data)})