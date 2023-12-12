from pydantic import BaseModel
from datetime import *

class param_personas(BaseModel):
    l_codigo: str
    l_apellido_paterno: str
    l_apellido_materno: str
    l_nombres: str
    l_razon_social: str
    l_tipo_documento: str
    l_numero_documento: str
    l_pais: str
    l_nacionalidad: str
    l_ciudad: str
    l_estado_civil: str
    l_sexo: str
    l_fecha_nacimiento: date
    l_lugar_nacimiento: str
    l_correo: str
    l_provincia: str
    l_canton: str
    l_parroquia: str
    l_direccion: str
    l_celular: str
    l_telefono: str