from fastapi import APIRouter

# from app.api.v1.routes.demo import demo_router
# from app.api.v1.routes.status import status_router
# from app.api.v1.routes.test import test_router
from app.api.v1.routes.macsys_dynamics import macsys_dynamics_router
from app.api.v1.routes.libelula_dynamics import libelula_dynamics_router
from app.api.v1.routes.libelula_macsys import libelula_macsys_router

api_v1 = APIRouter()

# api_v1.include_router(
#     status_router,
#     prefix='/status',
#     tags=['Servicios Web de status del servidor']
# )

# api_v1.include_router(
#     demo_router,
#     prefix='/demo',
#     tags=['Servicios DEMO para conexion con IBM Informix']
# )

# api_v1.include_router(
#     test_router,
#     prefix='/test',
#     tags=['Rutas para realizar pruebas']
# )

api_v1.include_router(
    macsys_dynamics_router,
    prefix='/macsys-dynamics',
    tags=['Servicios para Integración Macsys Dynamics']
)

api_v1.include_router(
    libelula_dynamics_router,
    prefix='/libelula-dynamics',
    tags=['Servicios para Integración Libelula Dynamics']
)

api_v1.include_router(
    libelula_macsys_router,
    prefix='/libelula-macsys',
    tags=['Servicios para Integración Libelula Macsys']
)