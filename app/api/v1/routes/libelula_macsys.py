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
    
@libelula_macsys_router.post('/persona-insertar')
def persona_insertar(param:param_persona):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta los datos correspondientes dentro de las diferentes tablas de Clientes.

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE informix.fn_lb_personas_insert(:l_codigo,:l_apellido_paterno,:l_apellido_materno,
                :l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,
                :l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,
                :l_parroquia,:l_direccion,:l_celular,:l_telefono);`
    - **Parámetros**:
        - l_apellido_paterno    str(50)
        - l_apellido_materno    str(50)
        - l_nombres             str(70)
        - l_razon_social        str(100)
        - l_tipo_documento      str(3)      {CED:CEDULA;RUC:RUC;PAS:PASAPORTE}
        - l_numero_documento    str(25)
        - l_pais                str(20)
        - l_nacionalidad        str(25)
        - l_ciudad              str(15)
        - l_estado_civil        str(1)      {C:Casado;S:Soltero;D:Divorciado;V:Viudo}
        - l_sexo                str(1)      {M:Masculino;F:Femenino}
        - l_fecha_nacimiento    str         yyyy-MM-dd hh:mm:ss.001
        - l_lugar_nacimiento    str(25)
        - l_correo              str(100)
        - l_provincia           str(5)      código de 2 dígitos
        - l_canton              str(5)      código de 2 dígitos
        - l_parroquia           str(5)      código de 2 dígitos
        - l_direccion           str(100)
        - l_celular             str(50)
        - l_telefono            str(50)
    - **Método HTTP**: `POST`
    - **Ruta**: `/persona-insertar`
    '''
    return LibelulaMacsysService.persona_insert(param)

@libelula_macsys_router.post('/persona-actualizar')
def persona_actualizar(param:param_persona):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza los datos correspondientes dentro de las diferentes tablas de Clientes.

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE informix.fn_lb_personas_update(:l_codigo,:l_apellido_paterno,:l_apellido_materno,
                :l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,
                :l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,
                :l_parroquia,:l_direccion,:l_celular,:l_telefono);`
    - **Parámetros**:
        - l_apellido_paterno    str(50)
        - l_apellido_materno    str(50)
        - l_nombres             str(70)
        - l_razon_social        str(100)
        - l_tipo_documento      str(3)      {CED:CEDULA;RUC:RUC;PAS:PASAPORTE}
        - l_numero_documento    str(25)
        - l_pais                str(20)
        - l_nacionalidad        str(25)
        - l_ciudad              str(15)
        - l_estado_civil        str(1)      {C:Casado;S:Soltero;D:Divorciado;V:Viudo}
        - l_sexo                str(1)      {M:Masculino;F:Femenino}
        - l_fecha_nacimiento    str         yyyy-MM-dd hh:mm:ss.001
        - l_lugar_nacimiento    str(25)
        - l_correo              str(100)
        - l_provincia           str(5)      código de 2 dígitos
        - l_canton              str(5)      código de 2 dígitos
        - l_parroquia           str(5)      código de 2 dígitos
        - l_direccion           str(100)
        - l_celular             str(50)
        - l_telefono            str(50)
    - **Método HTTP**: `POST`
    - **Ruta**: `/persona-actualizar`
    '''
    return LibelulaMacsysService.persona_update(param)

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

@libelula_macsys_router.post('/contrato-titular-insert')
def contrato_titular_insert(param:param_contrato_titular):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla T_CONTRATO_TITULARES del Macsys la relación entre el Contrato y el Titular

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE macsys.fn_lb_t_contrato_titulares_inserta(:v_IDCONTRATO,:v_IDTITULAR,
                            :v_BENEFICIO,:v_RENOVACION,:v_TIPO_COSTO,:v_VALOR);`
    - **Parámetros**:
        - v_IDCONTRATO      int(20)
        - v_IDENTIFICACION  str(13)
        - v_BENEFICIO       str(1)
        - v_RENOVACION      int(20)
        - v_TIPO_COSTO      int(20)
        - v_VALOR           float(18,2)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-titular-insert`
    '''
    return LibelulaMacsysService.contrato_titular_insert(param)

@libelula_macsys_router.post('/contrato-titular-update')
def contrato_titular_update(param:param_contrato_titular):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla T_CONTRATO_TITULARES del Macsys la relación entre el Contrato y el Titular

    ### Detalles Técnicos

    - **Procedimiento SQL**: `EXECUTE PROCEDURE macsys.fn_lb_t_contrato_titulares_update(:v_IDCONTRATO,:v_IDTITULAR,
                            :v_BENEFICIO,:v_RENOVACION,:v_TIPO_COSTO,:v_VALOR);`
    - **Parámetros**:
        - v_IDCONTRATO      int(20)
        - v_IDENTIFICACION  str(13)
        - v_BENEFICIO       str(1)
        - v_RENOVACION      int(20)
        - v_TIPO_COSTO      int(20)
        - v_VALOR           float(18,2)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-titular-update`
    '''
    return LibelulaMacsysService.contrato_titular_update(param)

@libelula_macsys_router.post('/contrato-beneficiario-insert')
def contrato_beneficiario_insert(param:param_contrato_beneficiario):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla T_CONTRATO_BENEFICIARIOS del Macsys la relación entre el Contrato y los Beneficarios

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_beneficiarios_insertar(:v_IDCONTRATO,:v_IDTITULAR,
               :v_IDBENEFICIARIO,:v_IDPLAN,:v_CUOTAS,:v_FECHA_INICIO,:v_maternidad,:v_renovacion,:v_tipo_ben);`
    - **Parámetros**:
        - v_IDCONTRATO      int(20)
        - v_IdentificadorTitular        str(13)
        - v_IdentificadorBeneficiario    str(13)
        - v_IDPLAN          str(4)
        - v_CUOTAS          int(20)
        - v_FECHA_INICIO    str         yyyy-MM-dd hh:mm:ss.001
        - v_maternidad      str(1)
        - v_renovacion      int(18)
        - v_tipo_ben        int(18)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-beneficiario-insert`
    '''
    return LibelulaMacsysService.contrato_beneficiario_insert(param)

@libelula_macsys_router.post('/contrato-beneficiario-update')
def contrato_beneficiario_update(param:param_contrato_beneficiario):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla T_CONTRATO_BENEFICIARIOS del Macsys la relación entre el Contrato y los Beneficarios

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_beneficiarios_update(:v_IDCONTRATO,:v_IDTITULAR,
               :v_IDBENEFICIARIO,:v_IDPLAN,:v_CUOTAS,:v_FECHA_INICIO,:v_maternidad,:v_renovacion,:v_tipo_ben);`
    - **Parámetros**:
        - v_IDCONTRATO      int(20)
        - v_IdentificadorTitular        str(13)
        - v_IdentificadorBeneficiario    str(13)
        - v_IDPLAN          str(4)
        - v_CUOTAS          int(20)
        - v_FECHA_INICIO    str         yyyy-MM-dd hh:mm:ss.001
        - v_maternidad      str(1)
        - v_renovacion      int(18)
        - v_tipo_ben        int(18)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-beneficiario-update`
    '''
    return LibelulaMacsysService.contrato_beneficiario_update(param)

@libelula_macsys_router.post('/contrato-cuota-insert')
def contrato_cuota_insert(param:param_contrato_cuotas):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla T_CONTRATO_CUOTAS del Macsys la relación entre el Contrato y las Cuotas

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_cuotas_inserta(:v_Idcontrato,:v_Idcliente,:v_fecha_contrato,
               :v_fecha_vencimiento,:v_cuota,:v_valor,:v_renovacion,:v_abono_ajus,:v_porc_desc,:v_fecha_des);`
    - **Parámetros**:
        - v_Idcontrato  int
        - v_IdentificadorCliente    str(13)
        - v_fecha_contrato  str yyyy-MM-dd hh:mm:ss.001
        - v_fecha_vencimiento   str yyyy-MM-dd hh:mm:ss.001
        - v_cuota   int
        - v_valor    float
        - v_renovacion  int
        - v_abono_ajus  float
        - v_porc_desc   float
        - v_fecha_des   str yyyy-MM-dd hh:mm:ss.001
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-cuota-insert`
    '''
    return LibelulaMacsysService.contrato_cuota_insert(param)

@libelula_macsys_router.post('/contrato-cuota-update')
def contrato_cuota_update(param:param_contrato_cuotas):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla T_CONTRATO_CUOTAS del Macsys la relación entre el Contrato y las Cuotas

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_cuotas_update(:v_Idcontrato,:v_renovacion,:v_Idcliente,:v_fecha_contrato,
               :v_fecha_vencimiento,:v_cuota,:v_valor,:v_abono_ajus,:v_porc_desc,:v_fecha_des);`
    - **Parámetros**:
        - v_Idcontrato  int
        - v_IdentificadorCliente    str(13)
        - v_fecha_contrato  str yyyy-MM-dd hh:mm:ss.001
        - v_fecha_vencimiento   str yyyy-MM-dd hh:mm:ss.001
        - v_cuota   int
        - v_valor    float
        - v_renovacion  int
        - v_abono_ajus  float
        - v_porc_desc   float
        - v_fecha_des   str yyyy-MM-dd hh:mm:ss.001
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-cuota-update`
    '''
    return LibelulaMacsysService.contrato_cuota_update(param)

@libelula_macsys_router.post('/contrato-banco-insert')
def contrato_banco_insert(param:param_contrato_banco):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla t_contrato_banco del Macsys la relación entre el Contrato y los Bancos

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_banco_insert(:v_IDCONTRATO,:v_renovacion,:v_banco,:v_tipo_cuenta_banco,
               ":v_numero_cuenta_banco);`
    - **Parámetros**:
        - v_IDCONTRATO          int
        - v_renovacion          int
        - v_banco               str(10)
        - v_tipo_cuenta_banco   str(1)
        - v_numero_cuenta_banco   str(20)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-banco-insert`
    '''
    return LibelulaMacsysService.contrato_banco_insert(param)

@libelula_macsys_router.post('/contrato-banco-update')
def contrato_banco_update(param:param_contrato_banco):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla t_contrato_banco del Macsys la relación entre el Contrato y los Bancos

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_banco_update(:v_IDCONTRATO,:v_renovacion,:v_banco,:v_tipo_cuenta_banco,
               ":v_numero_cuenta_banco);`
    - **Parámetros**:
        - v_IDCONTRATO          int
        - v_renovacion          int
        - v_banco               str(10)
        - v_tipo_cuenta_banco   str(1)
        - v_numero_cuenta_banco   str(20)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-banco-update`
    '''
    return LibelulaMacsysService.contrato_banco_update(param)

@libelula_macsys_router.post('/contrato-documento-insert')
def contrato_documento_insert(param:param_contrato_documento):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla t_contrato_documen del Macsys la relación entre el Contrato y los Documentos

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_documen_insert(:v_IDCONTRATO,:v_RENOVACION,:v_tipo,:v_documen,
               :v_observa,:v_fecha);`
    - **Parámetros**:
        - v_IDCONTRATO  int
        - v_RENOVACION  int
        - v_tipo        str(5)
        - v_documen     str(5)
        - v_observa     str(150)
        - v_fecha       str yyyy-MM-dd hh:mm:ss.001
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-documento-insert`
    '''
    return LibelulaMacsysService.contrato_documento_insert(param)

@libelula_macsys_router.post('/contrato-documento-update')
def contrato_documento_update(param:param_contrato_documento):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla t_contrato_documen del Macsys la relación entre el Contrato y los Documentos

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_t_contrato_documen_update(:v_IDCONTRATO,:v_RENOVACION,:v_tipo,:v_documen,
               :v_observa,:v_fecha);`
    - **Parámetros**:
        - v_IDCONTRATO  int
        - v_RENOVACION  int
        - v_tipo        str(5)
        - v_documen     str(5)
        - v_observa     str(150)
        - v_fecha       str yyyy-MM-dd hh:mm:ss.001
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-documento-insert`
    '''
    return LibelulaMacsysService.contrato_documento_update(param)

@libelula_macsys_router.post('/preexistencia-cliente-insert')
def preexistencia_cliente_insert(param:param_preexistencia_cliente):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla r_preexistencia_cliente del Macsys las preexistencia del Titular y Beneficiarios

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_r_preexistencia_cliente_insertar(:v_cliente,:v_iddiag,:v_fecha_pre,
               :v_observacion,:v_perma);`
    - **Parámetros**:
        - v_identificacion_cliente  str(13) [Identificación del Cliente]
        - v_iddiag          str(10) [Código de Diagnósitco]
        - v_fecha_pre       str yyyy-MM-dd hh:mm:ss.001 [Fecha de Inicio de la Preexistencia]
        - v_observacion     str(100)
        - v_perma           int
    - **Método HTTP**: `POST`
    - **Ruta**: `/preexistencia-cliente-insert`
    '''
    return LibelulaMacsysService.preexistencia_cliente_insert(param)

@libelula_macsys_router.post('/preexistencia-cliente-update')
def preexistencia_cliente_update(param:param_preexistencia_cliente):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla r_preexistencia_cliente del Macsys las preexistencia del Titular y Beneficiarios

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE macsys.fn_lb_r_preexistencia_cliente_update(:v_cliente,:v_iddiag,:v_fecha_pre,
               :v_observacion,:v_perma);`
    - **Parámetros**:
        - v_identificacion_cliente  str(13) [Identificación del Cliente]
        - v_iddiag          str(10) [Código de Diagnósitco]
        - v_fecha_pre       str yyyy-MM-dd hh:mm:ss.001 [Fecha de Inicio de la Preexistencia]
        - v_observacion     str(100)
        - v_perma           int
    - **Método HTTP**: `POST`
    - **Ruta**: `/preexistencia-cliente-update`
    '''
    return LibelulaMacsysService.preexistencia_cliente_insert(param)

@libelula_macsys_router.post('/contrato-insert')
def contrato_insert(param:param_contrato):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Inserta en la Tabla T_CONTRATO del Macsys los datos del Contrato a Generar

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE informix.fn_lb_t_contrato_insert(:v_IDCONTRATO,:v_IDTIPOCONTRATO,:v_FECHAAPERTURA,:v_cliente,
               :v_PERIODODESDE,:v_PERIODOHASTA,:v_IDVENDEDOR,:v_IDFORMAPAGO,:v_DIRECCIONCOBRO,:v_ESTADO,:v_RENOVACION,:v_OBSERVACION,
               :v_direccionDomicilio,:v_telefonoDomicilio,:v_direccionTrabajo,:v_telefonoTrabajo,:v_numero_beneficiarios,:v_idsupervisor,
               :v_forma_pago_c);`
    - **Parámetros**:
        - v_idcontrato: int(20)
        - v_idtipocontraro: str(2)
        - v_fechaapertura: str yyyy-MM-dd hh:mm:ss.001
        - v_ident_cliente: str (13)
        - v_periododesde: str yyyy-MM-dd hh:mm:ss.001
        - v_periodohasta: str yyyy-MM-dd hh:mm:ss.001
        - v_vendedor: 
            - v_identificacion: str (13)
            - v_nombre: str (100)
            - v_correo: str (50)   
        - v_idformapago: str(5)
        - v_direccioncobro: str(150)
        - v_estado: str(10)
        - v_renovacion: int
        - v_observacion: str(255)
        - v_direccionDomicilio: str(200)
        - v_telefonoDomicilio: str(50)
        - v_direccionTrabajo: str(200)
        - v_telefonoTrabajo: str(50)
        - v_numero_beneficiarios: int
        - v_supervisor:
            - v_identificacion: str (13)
            - v_nombre: str (100)
            - v_correo: str (50)              
        - v_forma_pago_c: str(3)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-insert`
    '''
    return LibelulaMacsysService.contrato_insert(param)

@libelula_macsys_router.post('/contrato-update')
def contrato_update(param:param_contrato):
    '''
    Integración desde Libelula hacia el Macsys

    ### Descripción

    Actualiza en la Tabla T_CONTRATO del Macsys los datos del Contrato

    ### Detalles Técnicos

    - **Procedimiento SQL**: `"EXECUTE PROCEDURE informix.fn_lb_t_contrato_update(:v_IDCONTRATO,:v_IDTIPOCONTRATO,:v_FECHAAPERTURA,:v_cliente,
               :v_PERIODODESDE,:v_PERIODOHASTA,:v_IDVENDEDOR,:v_IDFORMAPAGO,:v_DIRECCIONCOBRO,:v_ESTADO,:v_RENOVACION,:v_OBSERVACION,
               :v_direccionDomicilio,:v_telefonoDomicilio,:v_direccionTrabajo,:v_telefonoTrabajo,:v_numero_beneficiarios,:v_idsupervisor,
               :v_forma_pago_c);`
    - **Parámetros**:
        - v_idcontrato: int(20)
        - v_idtipocontraro: str(2)
        - v_fechaapertura: str yyyy-MM-dd hh:mm:ss.001
        - v_ident_cliente: str (13)
        - v_periododesde: str yyyy-MM-dd hh:mm:ss.001
        - v_periodohasta: str yyyy-MM-dd hh:mm:ss.001
        - v_vendedor: 
            - v_identificacion: str (13)
            - v_nombre: str (100)
            - v_correo: str (50)   
        - v_idformapago: str(5)
        - v_direccioncobro: str(150)
        - v_estado: str(10)
        - v_renovacion: int
        - v_observacion: str(255)
        - v_direccionDomicilio: str(200)
        - v_telefonoDomicilio: str(50)
        - v_direccionTrabajo: str(200)
        - v_telefonoTrabajo: str(50)
        - v_numero_beneficiarios: int
        - v_supervisor:
            - v_identificacion: str (13)
            - v_nombre: str (100)
            - v_correo: str (50)              
        - v_forma_pago_c: str(3)
    - **Método HTTP**: `POST`
    - **Ruta**: `/contrato-update`
    '''
    return LibelulaMacsysService.contrato_update(param)