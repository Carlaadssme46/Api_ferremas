from fastapi import FastAPI
from app.routers import ofertas, sucursal
from .database import engine,Base


app= FastAPI(
    description="api de ferreteria oferta sucursal",
    title="Ferremas",
    version="0.0.1"
)

Base.metadata.create_all(bind=engine)

app.include_router(ofertas.routerOferta)
app.include_router(sucursal.routerSucursal)
