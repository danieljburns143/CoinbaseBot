#!/usr/bin/env python3

import json

from autobahn.twisted.websocket import WebSocketClientProtocol

class ClientProtocol(WebSocketClientProtocol):

	def __init__(self):
		self.subscribeMessage =	{
			'type': 'subscribe',
			'channels': [
				{
					'name': 'matches',
					'product_ids': [
						'BTC-USD'
					]
				}
			]
		}

	def onConnect(self, response):
		print('Server connected: {}'.format(response.peer))

	def onOpen(self):
		print('Server connection opened')
		self.sendMessage(json.dumps(self.subscribeMessage).encode('utf8'))

	def onMessage(self, payload, isBinary):
		payload = json.loads(payload.decode('utf8'))
		if payload['type'] == 'match':
			self.parseMatchResponse(payload)
		else:
			print(payload)
	
	def onClose(self, wasClean, code, reason):
		if wasClean:
			print('Websocket connection closed cleanly: {}'.format(reason))
		else:
			print('Error... websocket connection closed uncleanly: {}'.format(reason))
	
	def parseMatchResponse(self, payload):
		print('Price: {}\tSide: {}'.format(payload['price'], payload['side']))
