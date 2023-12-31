from pydantic import BaseModel
from datetime import date

class FechaFiltro(BaseModel):
    v_fecha_desde: str
    v_fecha_hasta: str
    
    
class FechaCorte(BaseModel):
    v_fecha: str
    
class ParamValidarDiaIntegradoNd(BaseModel):
    dia: int
    mes: int
    anio: int
    nom_seccion: str