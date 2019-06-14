import usuario

class ActivePeers(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(ActivePeers, self).__new__(self)
            self.diccionario_de_usuarios = dict()                       #para usuarios comunes
            self.diccionario_usuarios_especiales = dict()               #para usarios sigesi y voip
            self.diccionario_usuarios_MIVoipRF = dict()
        return self._instance

    def addNewPeer(self,ip_key,usr_value):
        if(self.diccionario_de_usuarios.get(ip_key)==None):
            self.diccionario_de_usuarios.update({ip_key:usr_value})
            return "LOGUEO-EXITOSO"
        else:
            return "LOGUEO-EXISTENTE"
    def removePeer(self,ip):
        if(self.diccionario_de_usuarios.get(ip)!=None):
            self.diccionario_de_usuarios.pop(ip)
            return "USUARIO-DESLOGUEADO"
        else:
            return "USUARIO-INEXISTENTE"

    def getListaDeUsuariosConectados(self):
         res=[]
         for v in self.diccionario_de_usuarios.values():
             res.append(v.getNombre())
         return {"USUARIOS":res}
    
    def getListaDeSocketClientes(self):
        res=[]
        for v in self.diccionario_de_usuarios.values():
            res.append(v.getSocket())
        return res

    def getListaNombreIp(self):
        res=dict()
        for v in self.diccionario_de_usuarios.values():
            res.update({v.getNombre():v.getIp()})
        return res
