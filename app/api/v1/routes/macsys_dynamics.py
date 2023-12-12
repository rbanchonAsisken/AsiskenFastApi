from fastapi import APIRouter
from app.db.client import sp_return_list, select_return_list
from app.services.macsys_dynamics.models import *
from app.services.macsys_dynamics.service import *

macsys_dynamics_router=APIRouter()

@macsys_dynamics_router.get('/test')
def macsys_dynamics():
    return{
        "mensaje":"Grupo de APIs para Integrar Información del Macsys al Dynamics"
    }
    
@macsys_dynamics_router.post('/obtener-reembolsos')
def obtener_reembolsos(param:FechaCorte):
    '''
    Obtiene un listado de los reembolsos aprobados del Macsys.

    ### Descripción

    Esta operación recupera una lista completa de reembolsos aprobados por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_reembolso(:v_fecha);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-reembolsos`
    '''    
    return MacsysDynamicsService.obtener_reembolso(param)

@macsys_dynamics_router.post('/obtener-notacreditointerna')
def obtener_notas_creditos_interna(param:FechaFiltro):
    '''
    Obtiene un listado de las notas de crédito internas de Cxp por cruce de cuentas.

    ### Descripción

    Esta operación recupera una lista completa de Notas de Crédito Internas de Cxp por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_nota_credito_interna(:v_fecha_desde,:v_fecha_hasta);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-notacreditointerna`
    '''    
    return MacsysDynamicsService.obtener_nota_credito_interna_cxp(param)

@macsys_dynamics_router.post('/obtener-notacobranza')
def obtener_notas_cobranzas(param:FechaCorte):
    '''
    Obtiene un listado de las notas de cobranzas.

    ### Descripción

    Esta operación recupera una lista completa de las notas de cobranzas por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_nota_cobranza(:v_fecha);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-notacobranza`
    '''    
    return MacsysDynamicsService.obtener_nota_cobranza(param)

@macsys_dynamics_router.post('/obtener-facturaventacabecera')
def obtener_facturas_ventas_cabecera(param:FechaFiltro):
    '''
    Obtiene un listado de las Facturas de Ventas.

    ### Descripción

    Esta operación recupera la Cabecera para la Facturación por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_cabecera_fac_cxc(:v_fecha_desde,:v_fecha_hasta);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-facturaventacabecera`
    '''    
    return MacsysDynamicsService.obtener_factura_venta_cabecera(param)

@macsys_dynamics_router.post('/obtener-facturaventadetalle')
def obtener_facturas_ventas_detalle(param:FechaFiltro):
    '''
    Obtiene un listado de las Facturas de Ventas.

    ### Descripción

    Esta operación recupera el Detalle para la Facturación por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_detalle_fac_cxc(:v_fecha_desde,:v_fecha_hasta);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-facturaventadetalle`
    '''    
    return MacsysDynamicsService.obtener_factura_venta_detalle(param)

@macsys_dynamics_router.post('/obtener-facturacompracabecera')
def obtener_facturas_compras_cabecera(param:FechaCorte):
    '''
    Obtiene un listado de las Facturas de Liquidaciones de Prestadores.

    ### Descripción

    Esta operación recupera la Cabecera de Compras de Prestadores por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_cabecera_fac_cxp(:v_fecha_desde,:v_fecha_hasta);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-facturacompracabecera`
    '''    
    return MacsysDynamicsService.obtener_factura_compra_cabecera(param)

@macsys_dynamics_router.post('/obtener-facturacompradetalle')
def obtener_facturas_compras_detalle(param:FechaCorte):
    '''
    Obtiene un listado de las Facturas de Liquidaciones de Prestadores.

    ### Descripción

    Esta operación recupera el Detalle de Compras de Prestadores por Corte de Fecha.

    ### Detalles Técnicos

    - **Consulta SQL**: `EXECUTE PROCEDURE fn_detalle_fac_cxp(:v_fecha_desde,:v_fecha_hasta);`
    - **Formato de Parámetos de entrada**: `yyyy-MM-dd`
    - **Método HTTP**: `POST`
    - **Ruta**: `/obtener-facturacompradetalle`
    '''     
    return MacsysDynamicsService.obtener_factura_compra_detalle(param)