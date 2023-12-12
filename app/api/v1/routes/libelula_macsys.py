from fastapi import APIRouter
from app.db.client import sp_return_list, select_return_list
from app.services.libelula_macsys.models import *
from app.services.libelula_macsys.service import *

libelula_macsys_router=APIRouter()
    
@libelula_macsys_router.get('/test')
def libelula_macsys():
    return{
        "mensaje":"Grupo de APIs para Integrar Información entre Libelula y Macsys"
    }
    
@libelula_macsys_router.post('/clientes-insertar')
def clientes_insertar(param:param_personas):
    '''
    Integración de Clientes desde Libelula hacia el Macsys

    ### Descripción

    Inserta los datos correspondientes dentro de las diferentes tablas de Clientes.

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE informix.sp_lb_personas_insert(:l_codigo,:l_apellido_paterno,:l_apellido_materno,
                :l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,
                :l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,
                :l_parroquia,:l_direccion,:l_celular,:l_telefono);`
    - **Parámetros**:
        - l_codigo              str(18)
        - l_apellido_paterno    str(50)
        - l_apellido_materno    str(50)
        - l_nombres             str(70)
        - l_razon_social        str(100)
        - l_tipo_documento      str(3)
        - l_numero_documento    str(25)
        - l_pais                str(20)
        - l_nacionalidad        str(25)
        - l_ciudad              str(15)
        - l_estado_civil        str(1)
        - l_sexo                str(1)
        - l_fecha_nacimiento    DATETIME yyyy-MM-dd
        - l_lugar_nacimiento    str(25)
        - l_correo              str(100)
        - l_provincia           str(5)
        - l_canton              str(5)
        - l_parroquia           str(5)
        - l_direccion           str(100)
        - l_celular             str(50)
        - l_telefono            str(50)
    - **Método HTTP**: `POST`
    - **Ruta**: `/clientes-insertar`
    '''
    return LibelulaMacsysService.personas_insert(param)

@libelula_macsys_router.post('/clientes-actualizar')
def clientes_actualizar(param:param_personas):
    '''
    Integración de Clientes desde Libelula hacia el Macsys

    ### Descripción

    Actualiza los datos correspondientes dentro de las diferentes tablas de Clientes.

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE informix.sp_lb_personas_update(:l_codigo,:l_apellido_paterno,:l_apellido_materno,
                :l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,
                :l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,
                :l_parroquia,:l_direccion,:l_celular,:l_telefono);`
    - **Parámetros**:
        - l_codigo              str(18)
        - l_apellido_paterno    str(50)
        - l_apellido_materno    str(50)
        - l_nombres             str(70)
        - l_razon_social        str(100)
        - l_tipo_documento      str(3)
        - l_numero_documento    str(25)
        - l_pais                str(20)
        - l_nacionalidad        str(25)
        - l_ciudad              str(15)
        - l_estado_civil        str(1)
        - l_sexo                str(1)
        - l_fecha_nacimiento    DATETIME yyyy-MM-dd 
        - l_lugar_nacimiento    str(25)
        - l_correo              str(100)
        - l_provincia           str(5)
        - l_canton              str(5)
        - l_parroquia           str(5)
        - l_direccion           str(100)
        - l_celular             str(50)
        - l_telefono            str(50)
    - **Método HTTP**: `POST`
    - **Ruta**: `/clientes-actualizar`
    '''
    return LibelulaMacsysService.personas_update(param)

@libelula_macsys_router.post('/obtener-id-contrato')
def obtener_id_contrato():
    '''
    Obtener el ID del Contrato a utilizar en la nueva Póliza.

    ### Descripción

    Devuelve la secuencia del contrato que le sigue.

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE fn_obtiene_idcontrato();`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-id-contrato`
    '''
    return LibelulaMacsysService.obtener_id_contrato()