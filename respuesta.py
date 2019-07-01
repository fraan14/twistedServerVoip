import json
def GenerarRespuestaJson(rta , contenido = None):
    res = dict()
    res.update({"RESPUESTA":str(rta)})
    if(contenido!=None):
        res.update({"CONTENIDO":contenido})
    return json.dumps(res)