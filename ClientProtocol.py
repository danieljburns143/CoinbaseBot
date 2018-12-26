#!/usr/bin/env python3

from autobahn.twisted.websocket import WebSocketClientProtocol
import json

class ClientProtocol(WebSocketClientProtocol):

	def __init__(self):
		self.subscribeMessage = {
			'type': 'subscribe',
			'product_ids': [
				'BTC-USD',
			],
			'channels': [
				'matches',
			]
		}

	def onConnect(self, response):
		print('Server connected: {0}'.format(response.peer))

	def onOpen(self):
		print('Server connection opened')
		self.sendMessage(json.dumps(self.subscribeMessage).encode('utf8'))
	
	def onMessage(self, payload, isBinary):
		if isBinary:
			print('Binary message received: {0} bytes'.format(len(payload)))
		else:
			print('Text message received: {0}'.format(payload.decode('utf8')))
	
	def onClose(self, wasClean, code, reason):
		print('Websocket connection closed: {0}'.format(reason))
