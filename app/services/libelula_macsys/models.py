from pydantic import BaseModel
from datetime import *

class param_preexistencia_cliente(BaseModel):
    v_identificacion_cliente: str
    v_iddiag: str
    v_fecha_pre: str
    v_observacion: str
    v_perma: str

class param_persona(BaseModel):
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
    l_fecha_nacimiento: str
    l_lugar_nacimiento: str
    l_correo: str
    l_provincia: str
    l_canton: str
    l_parroquia: str
    l_direccion: str
    l_celular: str
    l_telefono: str
    
class response_macsys(BaseModel):
    v_procesoexitoso: int
    v_coderror: int
    v_mensaje: str
    
class param_contrato_titular(BaseModel):
    v_IDCONTRATO: int
    v_IDENTIFICACION: str
    v_BENEFICIO: str
    v_RENOVACION: int
    v_TIPO_COSTO: int
    v_VALOR: float
    
class param_contrato_beneficiario(BaseModel):
    v_IDCONTRATO: int
    v_IdentificadorTitular: str
    v_IdentificadorBeneficiario: str
    v_IDPLAN: str
    v_CUOTAS: int
    v_FECHA_INICIO: str
    v_maternidad: str
    v_renovacion: int
    v_tipo_ben: int
    
class param_contrato_cuotas(BaseModel):
    v_Idcontrato: int
    v_IdentificadorCliente: str
    v_fecha_contrato: str
    v_fecha_vencimiento: str
    v_cuota: int
    v_valor: float
    v_renovacion: int
    v_abono_ajus: float
    v_porc_desc: float
    v_fecha_des: str
    
class param_contrato_banco(BaseModel):
    v_IDCONTRATO: int
    v_renovacion: int
    v_banco: str    
    v_tipo_cuenta_banco: str
    v_numero_cuenta_banco: str
    
class param_contrato_documento(BaseModel):
    v_IDCONTRATO: int
    v_RENOVACION: int
    v_tipo: str
    v_documen: str
    v_observa: str
    v_fecha: str
 
class param_broker_busca(BaseModel):
    v_identificacion: str
    v_nombre: str
    v_correo: str
    
class param_vendedor_busca(BaseModel):
    v_identificacion: str
    v_nombre: str
    v_correo: str     
    
class param_contrato(BaseModel):
    v_idcontrato: int
    v_idtipocontraro: str
    v_fechaapertura: str
    v_ident_cliente: str
    v_periododesde: str
    v_periodohasta: str
    v_vendedor: param_vendedor_busca
    v_idformapago: str
    v_direccioncobro: str
    v_estado: str
    v_renovacion: int
    v_observacion: str
    v_direccionDomicilio: str
    v_telefonoDomicilio: str
    v_direccionTrabajo: str
    v_telefonoTrabajo: str
    v_numero_beneficiarios: int
    v_supervisor: param_broker_busca
    v_forma_pago_c: str
    