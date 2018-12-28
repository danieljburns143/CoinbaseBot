#!/usr/bin/env python3

import json

from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, \
	connectWS

class Client():
	
	def __init__(self, ClientProtocol, webSocketFeedUrl):
		self.ClientProtocol = ClientProtocol
		self.webSocketFeedUrl = webSocketFeedUrl
		self.factory = WebSocketClientFactory(webSocketFeedUrl)
		self.factory.protocol = self.ClientProtocol

	def startClient(self):
		connectWS(self.factory)
		reactor.run()
