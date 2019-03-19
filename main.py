import sys
sys.path.append(".")

import datetime
import time
import os
from twisted.python import log
from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory, ClientFactory, Protocol


import MessageClientProtocol as client
import MessageServerProtocol as server
import NeighborManager as neighbor


addresses = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']
gwAddresses = ['10.0.0.10', '10.0.0.11']
nm = neighbor.NeighborManager()

nm.myAddress = str(sys.argv[1])
nm.neighbors = addresses
nm.gateways = gwAddresses

#print("starting...",nm.neighborAddress )

if reactor.running:
    reactor.stop()
    
factory = protocol.ServerFactory()
factory.protocol = server.MessageServerProtocol
reactor.listenTCP(5555, factory)


#print("coming")

reactor.callLater(5,nm.senseNeighbors)

#client4.cManager.connectBest()
#time.sleep(10)
reactor.callLater(15, nm.send)
#nm.send()
#reactor.callInThread(nm.send)

reactor.run()
