from app.services.libelula_macsys.models import *
from app.db.client import *
import json

class LibelulaMacsysService():
    
    @staticmethod
    def persona_insert(param: param_persona) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:i_identificacion)")
        
        parameters={
            "i_identificacion":param.l_numero_documento
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        d3 = d2[0]
        # FIN DEL BLOQUE
        
        sql2 = ("EXECUTE PROCEDURE informix.fn_lb_personas_insert(:l_codigo,:l_apellido_paterno,:l_apellido_materno,"
               ":l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,"
               ":l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,"
               ":l_parroquia,:l_direccion,:l_celular,:l_telefono)")
        
        parameters2={
            "l_codigo":d3["codigo"].strip(),
            "l_apellido_paterno":param.l_apellido_paterno,
            "l_apellido_materno":param.l_apellido_materno,
            "l_nombres":param.l_nombres,
            "l_razon_social":param.l_razon_social,
            "l_tipo_documento":param.l_tipo_documento,
            "l_numero_documento":param.l_numero_documento,
            "l_pais":param.l_pais,
            "l_nacionalidad":param.l_nacionalidad,
            "l_ciudad":param.l_ciudad,
            "l_estado_civil":param.l_estado_civil,
            "l_sexo":param.l_sexo,
            "l_fecha_nacimiento":param.l_fecha_nacimiento,
            "l_lugar_nacimiento":param.l_lugar_nacimiento,
            "l_correo":param.l_correo,
            "l_provincia":param.l_provincia,
            "l_canton":param.l_canton,
            "l_parroquia":param.l_parroquia,
            "l_direccion":param.l_direccion,
            "l_celular":param.l_celular,
            "l_telefono":param.l_telefono
        }
        
        index_column_names2=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql2,parameters2,index_column_names2)                
    
    @staticmethod
    def persona_update(param: param_persona) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:i_identificacion)")
        
        parameters={
            "i_identificacion":param.l_numero_documento
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        d3 = d2[0]
        # FIN DEL BLOQUE
        
        sql2 = ("EXECUTE PROCEDURE informix.fn_lb_personas_update(:l_codigo,:l_apellido_paterno,:l_apellido_materno,"
               ":l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,"
               ":l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,"
               ":l_parroquia,:l_direccion,:l_celular,:l_telefono)")
        
        parameters2={
            "l_codigo":d3["codigo"].strip(),
            "l_apellido_paterno":param.l_apellido_paterno,
            "l_apellido_materno":param.l_apellido_materno,
            "l_nombres":param.l_nombres,
            "l_razon_social":param.l_razon_social,
            "l_tipo_documento":param.l_tipo_documento,
            "l_numero_documento":param.l_numero_documento,
            "l_pais":param.l_pais,
            "l_nacionalidad":param.l_nacionalidad,
            "l_ciudad":param.l_ciudad,
            "l_estado_civil":param.l_estado_civil,
            "l_sexo":param.l_sexo,
            "l_fecha_nacimiento":param.l_fecha_nacimiento,
            "l_lugar_nacimiento":param.l_lugar_nacimiento,
            "l_correo":param.l_correo,
            "l_provincia":param.l_provincia,
            "l_canton":param.l_canton,
            "l_parroquia":param.l_parroquia,
            "l_direccion":param.l_direccion,
            "l_celular":param.l_celular,
            "l_telefono":param.l_telefono
        }
        
        index_column_names2=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql2,parameters2,index_column_names2)    
    
    @staticmethod
    def obtener_id_contrato() -> list:
        
        sql = ("EXECUTE PROCEDURE fn_obtiene_idcontrato()")
        
        parameters={}
        
        index_column_names=[
            "numero"
        ]
        
        # return sp_return_list(sql,parameters,index_column_names)
        return sp_return_list(sql,None,index_column_names)     
    
    @staticmethod
    def contrato_titular_insert(param:param_contrato_titular) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:i_identificacion)")
        
        parameters={
            "i_identificacion":param.v_IDENTIFICACION
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL TITULAR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        d3 = d2[0]
        # FIN DEL BLOQUE        
        
        sql2 = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_titulares_inserta(:v_IDCONTRATO,:v_IDTITULAR,"
               ":v_BENEFICIO,:v_RENOVACION,:v_TIPO_COSTO,:v_VALOR)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_IDTITULAR":d3["codigo"].strip(),
            "v_BENEFICIO":param.v_BENEFICIO,
            "v_RENOVACION":param.v_RENOVACION,
            "v_TIPO_COSTO":param.v_TIPO_COSTO,
            "v_VALOR":param.v_VALOR
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)
    
    @staticmethod
    def contrato_titular_update(param:param_contrato_titular) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:i_identificacion)")
        
        parameters={
            "i_identificacion":param.v_IDENTIFICACION
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL TITULAR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        d3 = d2[0]
        # FIN DEL BLOQUE        
        
        sql2 = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_titulares_update(:v_IDCONTRATO,:v_IDTITULAR,"
               ":v_BENEFICIO,:v_RENOVACION,:v_TIPO_COSTO,:v_VALOR)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_IDTITULAR":d3["codigo"].strip(),
            "v_BENEFICIO":param.v_BENEFICIO,
            "v_RENOVACION":param.v_RENOVACION,
            "v_TIPO_COSTO":param.v_TIPO_COSTO,
            "v_VALOR":param.v_VALOR
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)
        
    @staticmethod
    def contrato_beneficiario_insert(param:param_contrato_beneficiario) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_IdentificadorTitular
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL TITULAR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dTitular = d2[0]
        # FIN DEL BLOQUE        
        
        parameters={
            "v_Identificador":param.v_IdentificadorBeneficiario
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL BENEFICIARIO
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dBeneficiario = d2[0]
        # FIN DEL BLOQUE    
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_beneficiarios_insertar(:v_IDCONTRATO,:v_IDTITULAR,"
               ":v_IDBENEFICIARIO,:v_IDPLAN,:v_CUOTAS,:v_FECHA_INICIO,:v_maternidad,:v_renovacion,:v_tipo_ben)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_IDTITULAR":dTitular["codigo"].strip(),
            "v_IDBENEFICIARIO":dBeneficiario["codigo"].strip(),
            "v_IDPLAN":param.v_IDPLAN,
            "v_CUOTAS":param.v_CUOTAS,
            "v_FECHA_INICIO":param.v_FECHA_INICIO,
            "v_maternidad":param.v_maternidad,
            "v_renovacion":param.v_renovacion,
            "v_tipo_ben":param.v_tipo_ben
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names) 
    
    @staticmethod
    def contrato_beneficiario_update(param:param_contrato_beneficiario) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_IdentificadorTitular
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL TITULAR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dTitular = d2[0]
        # FIN DEL BLOQUE        
        
        parameters={
            "v_Identificador":param.v_IdentificadorBeneficiario
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL BENEFICIARIO
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dBeneficiario = d2[0]
        # FIN DEL BLOQUE    
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_beneficiarios_update(:v_IDCONTRATO,:v_IDTITULAR,"
               ":v_IDBENEFICIARIO,:v_IDPLAN,:v_CUOTAS,:v_FECHA_INICIO,:v_maternidad,:v_renovacion,:v_tipo_ben)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_IDTITULAR":dTitular["codigo"].strip(),
            "v_IDBENEFICIARIO":dBeneficiario["codigo"].strip(),
            "v_IDPLAN":param.v_IDPLAN,
            "v_CUOTAS":param.v_CUOTAS,
            "v_FECHA_INICIO":param.v_FECHA_INICIO,
            "v_maternidad":param.v_maternidad,
            "v_renovacion":param.v_renovacion,
            "v_tipo_ben":param.v_tipo_ben
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names) 
        
    @staticmethod
    def contrato_cuota_insert(param:param_contrato_cuotas) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_IdentificadorCliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE        
        
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_cuotas_inserta(:v_Idcontrato,:v_Idcliente,:v_fecha_contrato,"
               ":v_fecha_vencimiento,:v_cuota,:v_valor,:v_renovacion,:v_abono_ajus,:v_porc_desc,:v_fecha_des)")        
        
        parameters={
            "v_Idcontrato":param.v_Idcontrato,
            "v_Idcliente":dCliente["codigo"].strip(),
            "v_fecha_contrato":param.v_fecha_contrato,
            "v_fecha_vencimiento":param.v_fecha_vencimiento,
            "v_cuota":param.v_cuota,
            "v_valor":param.v_valor,
            "v_renovacion":param.v_renovacion,
            "v_abono_ajus":param.v_abono_ajus,
            "v_porc_desc":param.v_porc_desc,
            "v_fecha_des":param.v_fecha_des
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)     
    
    @staticmethod
    def contrato_cuota_update(param:param_contrato_cuotas) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_IdentificadorCliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE        
        
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_cuotas_update(:v_Idcontrato,:v_renovacion,:v_Idcliente,"
               ":v_fecha_contrato,:v_fecha_vencimiento,:v_cuota,:v_valor,:v_abono_ajus,:v_porc_desc,:v_fecha_des)")        
        
        parameters={
            "v_Idcontrato":param.v_Idcontrato,
            "v_renovacion":param.v_renovacion,
            "v_Idcliente":dCliente["codigo"].strip(),
            "v_fecha_contrato":param.v_fecha_contrato,
            "v_fecha_vencimiento":param.v_fecha_vencimiento,
            "v_cuota":param.v_cuota,
            "v_valor":param.v_valor,
            "v_abono_ajus":param.v_abono_ajus,
            "v_porc_desc":param.v_porc_desc,
            "v_fecha_des":param.v_fecha_des
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)        
    
    @staticmethod
    def contrato_banco_insert(param:param_contrato_banco) -> list:
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_banco_insert(:v_IDCONTRATO,:v_renovacion,:v_banco,:v_tipo_cuenta_banco,"
               ":v_numero_cuenta_banco)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_renovacion":param.v_renovacion,
            "v_banco":param.v_banco,
            "v_tipo_cuenta_banco":param.v_tipo_cuenta_banco,
            "v_numero_cuenta_banco":param.v_numero_cuenta_banco
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)       
    
    @staticmethod
    def contrato_banco_update(param:param_contrato_banco) -> list:
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_banco_update(:v_IDCONTRATO,:v_renovacion,:v_banco,:v_tipo_cuenta_banco,"
               ":v_numero_cuenta_banco)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_renovacion":param.v_renovacion,
            "v_banco":param.v_banco,
            "v_tipo_cuenta_banco":param.v_tipo_cuenta_banco,
            "v_numero_cuenta_banco":param.v_numero_cuenta_banco
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)         
    
    @staticmethod
    def contrato_documento_insert(param:param_contrato_documento) -> list:
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_documen_insert(:v_IDCONTRATO,:v_RENOVACION,:v_tipo,:v_documen,"
               ":v_observa,:v_fecha)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_RENOVACION":param.v_RENOVACION,
            "v_tipo":param.v_tipo,
            "v_documen":param.v_documen,
            "v_observa":param.v_observa,
            "v_fecha":param.v_fecha
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)   
    
    @staticmethod
    def contrato_documento_update(param:param_contrato_documento) -> list:
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_t_contrato_documen_update(:v_IDCONTRATO,:v_RENOVACION,:v_tipo,:v_documen,"
               ":v_observa,:v_fecha)")        
        
        parameters={
            "v_IDCONTRATO":param.v_IDCONTRATO,
            "v_RENOVACION":param.v_RENOVACION,
            "v_tipo":param.v_tipo,
            "v_documen":param.v_documen,
            "v_observa":param.v_observa,
            "v_fecha":param.v_fecha
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)     
 
    @staticmethod
    def preexistencia_cliente_insert(param:param_preexistencia_cliente) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_identificacion_cliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE        
        
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_r_preexistencia_cliente_inserta(:v_cliente,:v_iddiag,:v_fecha_pre,"
               ":v_observacion,:v_perma)")        
        
        parameters={
            "v_cliente":dCliente["codigo"].strip(),
            "v_iddiag":param.v_fecha_contrato,
            "v_fecha_pre":param.v_fecha_vencimiento,
            "v_observacion":param.v_cuota,
            "v_perma":param.v_valor
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)     
    
    @staticmethod
    def preexistencia_cliente_update(param:param_preexistencia_cliente) -> list:
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_identificacion_cliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE        
        
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_r_preexistencia_cliente_update(:v_cliente,:v_iddiag,:v_fecha_pre,"
               ":v_observacion,:v_perma)")        
        
        parameters={
            "v_cliente":dCliente["codigo"].strip(),
            "v_iddiag":param.v_fecha_contrato,
            "v_fecha_pre":param.v_fecha_vencimiento,
            "v_observacion":param.v_cuota,
            "v_perma":param.v_valor
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)    
    
    @staticmethod
    def contrato_insert(param:param_contrato) -> list:
        
        vendedor=param.v_vendedor
        supervisor=param.v_supervisor
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_r_vendedor_busca(:v_identificacion,:v_nombre,:v_correo)")
        
        parameters={
            "v_Identificador":supervisor.v_identificacion,
            "v_nombre":supervisor.v_nombre,
            "v_correo":supervisor.v_correo
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL VENDEDOR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dVendedor = d2[0]
        # FIN DEL BLOQUE       
        
        sql = ("EXECUTE PROCEDURE informix.fn_lb_r_broker_busca(:v_identificacion,:v_nombre,:v_correo)")
        
        parameters={
            "v_Identificador":vendedor.v_identificacion,
            "v_nombre":vendedor.v_nombre,
            "v_correo":vendedor.v_correo
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL SUPERVISOR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dSupervisor = d2[0]
        # FIN DEL BLOQUE      
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_ident_cliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE             
        
        sql = ("EXECUTE PROCEDURE informix.fn_lb_t_contrato_insert(:v_IDCONTRATO,:v_IDTIPOCONTRATO,:v_FECHAAPERTURA,:v_cliente,"
               ":v_PERIODODESDE,:v_PERIODOHASTA,:v_IDVENDEDOR,:v_IDFORMAPAGO,:v_DIRECCIONCOBRO,:v_ESTADO,:v_RENOVACION,:v_OBSERVACION,"
               ":v_direccionDomicilio,:v_telefonoDomicilio,:v_direccionTrabajo,:v_telefonoTrabajo,:v_numero_beneficiarios,:v_idsupervisor,"
               ":v_forma_pago_c)")        
        
        parameters={
            "v_IDCONTRATO":param.v_idcontrato,
            "v_IDTIPOCONTRATO":param.v_idtipocontraro,
            "v_FECHAAPERTURA":param.v_fechaapertura,
            "v_cliente":dCliente["codigo"].strip(),
            "v_PERIODODESDE":param.v_periododesde,
            "v_PERIODOHASTA":param.v_periodohasta,
            "v_IDVENDEDOR":dVendedor["codigo"].strip(),
            "v_IDFORMAPAGO":param.v_idformapago,
            "v_DIRECCIONCOBRO":param.v_direccioncobro,
            "v_ESTADO":param.v_estado,
            "v_RENOVACION":param.v_renovacion,
            "v_OBSERVACION":param.v_observacion,
            "v_direccionDomicilio":param.v_direccionDomicilio,
            "v_telefonoDomicilio":param.v_telefonoDomicilio,
            "v_direccionTrabajo":param.v_direccionTrabajo,
            "v_telefonoTrabajo":param.v_telefonoTrabajo,
            "v_numero_beneficiarios":param.v_numero_beneficiarios,
            "v_idsupervisor":dSupervisor["codigo"].strip(),
            "v_forma_pago_c":param.v_forma_pago_c                                    
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)  
    
    @staticmethod
    def contrato_update(param:param_contrato) -> list:
        
        vendedor=param.v_vendedor
        supervisor=param.v_supervisor
        
        sql = ("EXECUTE PROCEDURE macsys.fn_lb_r_vendedor_busca(:v_identificacion,:v_nombre,:v_correo)")
        
        parameters={
            "v_Identificador":supervisor.v_identificacion,
            "v_nombre":supervisor.v_nombre,
            "v_correo":supervisor.v_correo
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL VENDEDOR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dVendedor = d2[0]
        # FIN DEL BLOQUE       
        
        sql = ("EXECUTE PROCEDURE informix.fn_lb_r_broker_busca(:v_identificacion,:v_nombre,:v_correo)")
        
        parameters={
            "v_Identificador":vendedor.v_identificacion,
            "v_nombre":vendedor.v_nombre,
            "v_correo":vendedor.v_correo
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL SUPERVISOR
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dSupervisor = d2[0]
        # FIN DEL BLOQUE      
        
        sql = ("EXECUTE PROCEDURE informix.fn_obtiene_idpersona(:v_Identificador)")
        
        parameters={
            "v_Identificador":param.v_ident_cliente
        }
        
        index_column_names=[
            "codigo"
        ]
        
        # ESTE BLOQUE RECUPERA EL CÓDIGO EXISTENTE DEL CLIENTE
        retorno=sp_return_list(sql,parameters,index_column_names) 
        s1 = json.dumps(retorno)
        d2 = json.loads(s1)
        dCliente = d2[0]
        # FIN DEL BLOQUE             
        
        sql = ("EXECUTE PROCEDURE informix.fn_lb_t_contrato_update(:v_IDCONTRATO,:v_IDTIPOCONTRATO,:v_FECHAAPERTURA,:v_cliente,"
               ":v_PERIODODESDE,:v_PERIODOHASTA,:v_IDVENDEDOR,:v_IDFORMAPAGO,:v_DIRECCIONCOBRO,:v_ESTADO,:v_RENOVACION,:v_OBSERVACION,"
               ":v_direccionDomicilio,:v_telefonoDomicilio,:v_direccionTrabajo,:v_telefonoTrabajo,:v_numero_beneficiarios,:v_idsupervisor,"
               ":v_forma_pago_c)")        
        
        parameters={
            "v_IDCONTRATO":param.v_idcontrato,
            "v_IDTIPOCONTRATO":param.v_idtipocontraro,
            "v_FECHAAPERTURA":param.v_fechaapertura,
            "v_cliente":dCliente["codigo"].strip(),
            "v_PERIODODESDE":param.v_periododesde,
            "v_PERIODOHASTA":param.v_periodohasta,
            "v_IDVENDEDOR":dVendedor["codigo"].strip(),
            "v_IDFORMAPAGO":param.v_idformapago,
            "v_DIRECCIONCOBRO":param.v_direccioncobro,
            "v_ESTADO":param.v_estado,
            "v_RENOVACION":param.v_renovacion,
            "v_OBSERVACION":param.v_observacion,
            "v_direccionDomicilio":param.v_direccionDomicilio,
            "v_telefonoDomicilio":param.v_telefonoDomicilio,
            "v_direccionTrabajo":param.v_direccionTrabajo,
            "v_telefonoTrabajo":param.v_telefonoTrabajo,
            "v_numero_beneficiarios":param.v_numero_beneficiarios,
            "v_idsupervisor":dSupervisor["codigo"].strip(),
            "v_forma_pago_c":param.v_forma_pago_c                                    
        }
        
        index_column_names=[
            "v_procesoexitoso",
            "v_coderror",
            "v_mensaje"
        ]
        
        return sp_return_list(sql,parameters,index_column_names)  