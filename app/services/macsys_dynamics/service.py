from app.services.macsys_dynamics.models import *
from app.db import client, clientSQL


class MacsysDynamicsService():
    
####### LLAMADO A PROCEDIMIENTOS INFORMIX
    
    @staticmethod
    def obtener_reembolso(fecha:FechaCorte) -> list:
        
        sql = "EXECUTE PROCEDURE fn_reembolso(:v_fecha);"
        
        parameters={
            "v_fecha":fecha.v_fecha
        }
        
        index_column_names = [
            "nombre_lib_diario",
            "nombre_seccion",
            "linea",
            "tipo_mov",
            "n_cuenta",
            "fecha_registro",
            "tipo_documento",
            "n_documento",
            "descripcion",
            "tipo_partida",
            "cta_contrapartida",
            "importe",
            "userdef1",
            "userdef2",
            "userdef3",
            "userdef4",
            "userdef5",
            "userdef6",
            "tipoliquidacion",
            "numero_liquidacion",
            "contrato",
            "area_code",
            "canal_code",
            "ceco_code",
            "clase_code",
            "departamento",
            "division_code",
            "lineas_code",
            "nombre_plan",
            "region",
            "tipo_code",
            "estado_reembolso"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)
    
    @staticmethod
    def obtener_nota_credito_interna_cxp(param:FechaFiltro) -> list:
        
        sql = "EXECUTE PROCEDURE fn_nota_credito_interna(:v_fecha_desde,:v_fecha_hasta);"
        
        parameters={
            "v_fecha_desde":param.v_fecha_desde,
            "v_fecha_hasta":param.v_fecha_hasta
        }
        
        index_column_names = [
            "nombre_lib_diario",
            "nombre_seccion",
            "linea",
            "tipo_mov",
            "n_cuenta",
            "fecha_registro",
            "tipo_documento",
            "n_documento",
            "descripcion",
            "tipo_partida",
            "cta_contrapartida",
            "importe",
            "userdef1",
            "userdef2",
            "userdef3",
            "userdef4",
            "userdef5",
            "userdef6",
            "tipoliquidacion",
            "numero_liquidacion",
            "contrato",
            "area_code",
            "canal_code",
            "ceco_code",
            "clase_code",
            "departamento",
            "division_code",
            "lineas_code",
            "nombre_plan",
            "region",
            "tipo_code"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)
    
    @staticmethod
    def obtener_nota_cobranza(fecha:FechaCorte) -> list:
        
        sql = "EXECUTE PROCEDURE fn_nota_cobranza(:v_fecha);"
        
        parameters={
            "v_fecha":fecha.v_fecha
        }
        
        index_column_names = [
            "nombre_lib_diario",
            "nombre_seccion",
            "linea",
            "tipo_mov",
            "n_cuenta",
            "fecha_registro",
            "tipo_documento",
            "n_documento",
            "descripcion",
            "tipo_partida",
            "cta_contrapartida",
            "importe",
            "userdef1",
            "userdef2",
            "userdef3",
            "userdef4",
            "userdef5",
            "userdef6",
            "tipoliquidacion",
            "numero_liquidacion",
            "contrato",
            "area_code",
            "canal_code",
            "ceco_code",
            "clase_code",
            "departamento",
            "division_code",
            "lineas_code",
            "nombre_plan",
            "region",
            "tipo_code"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)    
    
    @staticmethod
    def obtener_factura_venta_cabecera(param:FechaFiltro) -> list:
        
        sql = "EXECUTE PROCEDURE fn_cabecera_fac_cxc(:v_fecha_desde,:v_fecha_hasta);"
        
        parameters={
            "v_fecha_desde": param.v_fecha_desde,
            "v_fecha_hasta": param.v_fecha_hasta
        }
        
        index_column_names = [
            "idcontrato",
            "renovacion",
            "tipo_documento",
            "numero",
            "numero_cedula",
            "fecha_pedido",
            "fecha_registro",
            "cod_termino_pago",
            "cod_almacen",
            "tipotransaccion",
            "tipocomprobante",
            "formapago",
            "iddocsri",
            "userdef1",
            "userdef2",
            "userdef3",
            "userdef4",
            "userdef5",
            "userdef6",
            "userdef7",
            "userdef8",
            "numero_contrato"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)  
    
    @staticmethod
    def obtener_factura_venta_detalle(param:FechaFiltro) -> list:
        
        sql = "EXECUTE PROCEDURE fn_detalle_fac_cxc(:v_fecha_desde,:v_fecha_hasta);"
        
        parameters={
            "v_fecha_desde": param.v_fecha_desde,
            "v_fecha_hasta": param.v_fecha_hasta
        }
        
        index_column_names = [
            "idcontrato",
            "renovacion",
            "tipo_documento",
            "numero",
            "linea",
            "cedula_ruc",
            "tipo",
            "no_",
            "cod_almacen",
            "descripcion",
            "unidad_medida",
            "cantidad",
            "precio_unitario",
            "descuento_linea",
            "importe_linea",
            "id_grupo_id",
            "ceco_code",
            "clase_code",
            "lineas_code",
            "nombre_plan",
            "canal_code",
            "tipo_ceco_code",
            "division_code",
            "region_code",
            "departamentocode",
            "areacode",
            "cuota",
            "fecha_cuota"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)  
    
    @staticmethod
    def obtener_factura_compra_cabecera(param:FechaCorte) -> list:
        
        sql = "EXECUTE PROCEDURE fn_cabecera_fac_cxp(:v_fecha_desde,:v_fecha_hasta);"
        
        parameters={
            "v_fecha_desde": param.v_fecha,
            "v_fecha_hasta": param.v_fecha
        }
        
        index_column_names = [
            "tipo_documento",
            "numero",
            "ruc",
            "fecha_pedido",
            "fecha_registro",
            "fecha_recepcion",
            "fecha_pp",
            "cod_almacen",
            "no_serie",
            "tipo_sustento",
            "tipo_compro",
            "autorizacion",
            "factura",
            "siniestro",
            "estado",
            "num_cart_aut",
            "numero_poliza",
            "tipo_liquidacion",
            "userdef6",
            "userdef7",
            "userdef8",
            "subtotal_0",
            "descuento_0",
            "subtotal_imp",
            "descuento_imp",
            "valor_imp",
            "valor_factura"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)  
    
    @staticmethod
    def obtener_factura_compra_detalle(param:FechaCorte) -> list:
        
        sql = "EXECUTE PROCEDURE fn_detalle_fac_cxp(:v_fecha_desde,:v_fecha_hasta);"
        
        parameters={
            "v_fecha_desde": param.v_fecha,
            "v_fecha_hasta": param.v_fecha
        }
        
        index_column_names = [
            "tipo_documento",
            "numero",
            "linea",
            "ruc",
            "tipo",
            "servicio_compra",
            "cod_almacen",
            "descripcion",
            "unidad_medida",
            "cantidad",
            "costo",
            "importe",
            "porc_desc_pp",
            "porc_desc",
            "valor_desc_pp",
            "valor_desc_comer",
            "costo_c",
            "c_tecnico",
            "tipo_producto",
            "plan",
            "canal",
            "honorarios",
            "div_code",
            "reg_code",
            "dpto_code",
            "area_code"
        ]
        
        return client.sp_return_list(sql, parameters, index_column_names)      
    
    
####### LLAMADO A PROCEDIMIENTOS EN EL SQL SERVER

    @staticmethod
    def validar_dia_integrado(param:ParamValidarDiaIntegradoNd) -> list:
        
        sql = "exec sp_obtener_nd_integrado :dia,:mes,:anio,:nom_seccion "
        
        parameters={
            "dia": param.dia,
            "mes": param.mes,
            "anio": param.anio,
            "nom_seccion": param.nom_seccion
        }
        
        index_column_names = [
            "mensaje",
            "fecha"
        ]
        
        return clientSQL.sp_return_list(sql, parameters, index_column_names)      