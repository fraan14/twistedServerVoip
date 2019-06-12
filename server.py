import sys 
import json
import peers
import procesadorMensajes
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, ClientFactory, Protocol 


class EchoServerProtocol(Protocol):
    def connectionMade(self):
        log.msg('Se establecio una conexion con:{}'.format(self.transport.getPeer()))
        #ip = self.transport.getPeer().host
        
        self.transport.setTcpKeepAlive(1)

    def dataReceived(self,data):
        guardar = peers.ActivePeers()
        #procesar mensaje
        #if (not "quit" in data):
            #text = json.loads(data)
            #log.msg("Cantidad de peers: {}".format(len(guardar.clientDictionary)))
            #log.msg('Logueo de: '+text["NOMBRE"])
            #v1 = text["NOMBRE"]
            #fin Procesar Mensaje
            #guardar.clientDictionary.update({self:v1})
        #ip = self.transport.hostname
        respuesta = procesadorMensajes.procesarMensaje(data,self)
        self.transport.write(respuesta.encode())
        #self.transport.write(guardar.getListStringValues().encode())
        #self.transport.write(json.dumps(guardar.getPublicDict()).encode())
        #log.msg("Clientes activos:{} ".format(guardar.getListStringValues()))
    
    def connectionLost(self,data):
        g = peers.ActivePeers()
        
        finsesion = procesadorMensajes.procesarFinSesion(self)
        lista_conectados = json.dumps(g.getListaDeUsuariosConectados())
        lista_sockets = g.getListaDeSocketClientes()
        for s in lista_sockets:
            s.transport.write(lista_conectados.encode())
        #g = peers.ActivePeers()
        #g.removePeer(self)
        #l = g.getConnectedClientsList()
        #newConnected = json.dumps(g.getPublicDict())
        #for c in l:
        #    c.transport.write(toret.encode())
        #log.msg("Clientes activos luego de deslogueo: {}".format(g.getListStringValues()))

class EchoServerFactory(ServerFactory):
    def buildProtocol(self,addr):
        return EchoServerProtocol()


def main():
    log.startLogging(sys.stdout)
    log.msg('Comenzando ejecucion...')
    reactor.listenTCP(16000, EchoServerFactory())
    reactor.run()

if __name__ == '__main__':
    main()
