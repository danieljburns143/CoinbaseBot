#!/usr/bin/env python3

class Client():
	
	def __init__(self, ClientProtocol, product_ids=[], channels=[]):
		self.ClientProtocol = ClientProtocol
		self.product_ids = product_ids
		self.channels = {}
		for channel in channels:
			self.channels[channel] = self.product_ids
	
	def addToIndividualChannel(self, channel, product_ids=[]):
		self.channels[channel] = self.product_ids
		for product_id in product_ids:
			self.channels[channel].append(product_id)
