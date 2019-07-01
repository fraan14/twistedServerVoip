import sys 
import json
import peers
import respuesta
import procesadorMensajes
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, ClientFactory, Protocol 


class EchoServerProtocol(Protocol):
    def connectionMade(self):
        log.msg('Se establecio una conexion con:{}'.format(self.transport.getPeer()))
        #ip = self.transport.getPeer().host
        res = respuesta.GenerarRespuestaJson("CONEXION-ESTABLECIDA")
        self.transport.write(res.encode())
        self.transport.setTcpKeepAlive(1)

    def dataReceived(self,data):
        guardar = peers.ActivePeers()
        respuesta = procesadorMensajes.procesarMensaje(data,self)
        self.transport.write(respuesta.encode())
    
    def connectionLost(self,data):
        g = peers.ActivePeers()
        
        finsesion = procesadorMensajes.procesarFinSesion(self)
        lista_conectados = json.dumps(g.getListaDeUsuariosConectados())
        lista_sockets = g.getListaDeSocketClientes()
        for s in lista_sockets:
            s.transport.write(lista_conectados.encode())
        log.msg('Se termino la conexion con:{}'.format(self.transport.getPeer()))

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
