import sys

class Usuario:

    def __init__(self):
        self.nombre = ""
        self.ip = ""
        self.socketTcp = None
        self.tipoConexion = ""
    def setNombre(self,nom):
        self.nombre = nom
    def setIp(self,ipp):
        self.ip=ipp
    def setSocketTcp(self,sock):
        self.socketTcp = sock
    def getNombre(self):
        return self.nombre
    def getIp(self):
        return self.ip
    def getSocket(self):
        return self.socketTcp
    def setTipoConexion(self,tipo):
        if(tipo.upper() == "VOZ"):
            self.tipoConexion = tipo
        else:
            if(tipo.upper() =="DATO"):
                self.tipoConexion = tipo
            else:
                if(tipo.upper() == "DUAL"):
                    self.tipoConexion = tipo
    
class UsuarioEspecial(Usuario):
    def __init__(self):
        Usuario.__init__(self)