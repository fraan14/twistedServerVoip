import usuario

class ActivePeers(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(ActivePeers, self).__new__(self)
            self.diccionario_de_usuarios = dict()
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
    # def getListStringValues(self):
    #     res=[]
    #     for v in self.clientDict.values():
    #         res.append(v)
    #     return {"USUARIOS":res}
    # def getConnectedClientsList(self):
    #     l = []
    #     for k in self.clientDict:
    #         l.append(k)
    #     return l