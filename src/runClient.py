#!/usr/bin/env python3

from ClientProtocol import *

import json

from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, \
	WebSocketClientProtocol, connectWS

if __name__ == '__main__':

	factory = WebSocketClientFactory('wss://ws-feed.pro.coinbase.com')
	factory.protocol = ClientProtocol

	connectWS(factory)
	reactor.run()
