import sys
import twisted.internet.interfaces
import json
import peers
import usuario

def procesarMensaje(mensaje, isock):
    #primero se trata de verificar que el mensaje sea un json
    #y que contenga tanto nombre como formato para poder identificarlo
    try:
        mensaje_json = json.loads(mensaje)
        nombre = mensaje_json["NOMBRE"]
        comando = mensaje_json['COMANDO']
    except: #aca va ael controlador de excepciones, si el mensaje no respeta el formato una respuesta es enviada al cliente indicando el formato del mensaje que se espera recibir
        return "error el en formato del mensaje, verifique su correctitud"
    if(comando == "LOGIN"):
        return procesarLogueo(mensaje_json, isock)
    if(comando == "LOGIN-ESPECIAL"):
        return procesarLogueoEspecial(mensaje_json,isock)
    if(comando == "FIN-SESION"):
        return procesarFinSesion(isock) 
    if(comando == "LISTA-CONECTADOS"):
        return procesarListaConectados()

def procesarLogueo(mensaje_json,isock):
    guardar = peers.ActivePeers()
    nombre = mensaje_json["NOMBRE"]
    ip = isock.transport.hostname
    usr = usuario.Usuario()
    usr.setNombre(nombre)
    usr.setIp(ip)
    usr.setSocketTcp(isock)
    return guardar.addNewPeer(nombre,usr)

def procesarLogueoEspecial(mensaje_json,isock):
    guardar = peers.ActivePeers()
    nombre = mensaje_json["NOMBRE"]
    ip = isock.transport.hostname
    usr = usuario.Usuario()
    usr.setNombre(nombre)
    usr.setIp(ip)
    usr.setSocketTcp(isock)
    return guardar.addNewSpecialPeer(ip,usr)
    
def procesarFinSesion(isock):
    guardar = peers.ActivePeers()
    ip = isock.transport.hostname
    return guardar.removePeer(ip)

def procesarListaConectados():
    guardar = peers.ActivePeers()
    return json.dumps(guardar.getListaNombreIp())
    

