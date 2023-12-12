from fastapi import APIRouter
from app.db.client import sp_return_list, select_return_list
from app.services.libelula_dynamics.models import *
from app.services.libelula_dynamics.service import *

libelula_dynamics_router=APIRouter()
    
@libelula_dynamics_router.get('/test')
def libelula_dynamics():
    return{
        "mensaje":"Grupo de APIs para Integrar Información entre Libelula y Dynamics"
    }