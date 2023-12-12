from app.services.libelula_macsys.models import *
from app.db.client import *

class LibelulaMacsysService():
    
    @staticmethod
    def personas_insert(param: param_personas) -> Any:
        
        sql = ("EXECUTE PROCEDURE informix.sp_lb_personas_insert(:l_codigo,:l_apellido_paterno,:l_apellido_materno,"
               ":l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,"
               ":l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,"
               ":l_parroquia,:l_direccion,:l_celular,:l_telefono)")
        
        parameters={
            "l_codigo":param.l_codigo,
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
        
        # index_column_names=[]
        
        # return sp_return_list(sql,parameters,index_column_names)
        return sp_return_one(sql,parameters)
    
    @staticmethod
    def personas_update(param: param_personas) -> Any:
        
        sql = ("EXECUTE PROCEDURE informix.sp_lb_personas_update(:l_codigo,:l_apellido_paterno,:l_apellido_materno,"
               ":l_nombres,:l_razon_social,:l_tipo_documento,:l_numero_documento,:l_pais,:l_nacionalidad,:l_ciudad,"
               ":l_estado_civil,:l_sexo,:l_fecha_nacimiento,:l_lugar_nacimiento,:l_correo,:l_provincia,:l_canton,"
               ":l_parroquia,:l_direccion,:l_celular,:l_telefono)")
        
        parameters={
            "l_codigo":param.l_codigo,
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
        
        # index_column_names=[]
        
        # return sp_return_list(sql,parameters,index_column_names)
        return sp_return_one(sql,parameters)    
    
    @staticmethod
    def obtener_id_contrato() -> list:
        
        sql = ("EXECUTE PROCEDURE fn_obtiene_idcontrato()")
        
        parameters={}
        
        index_column_names=[
            "numero"
        ]
        
        # return sp_return_list(sql,parameters,index_column_names)
        return sp_return_list(sql,None,index_column_names)     