#!/usr/bin/env python3

import requests
import json
import time

class RESTfulClient():

	def __init__(self):
		self.endpointURL = 'https://api.pro.coinbase.com'
	
	'''
	[
		{ 'id': 'x', 'base_currency': 'x', 'quote_currency': 'x', 'base_min_size': 'x',
		'base_max_size': 'x', 'quote_increment': 'x'}
	]
	'''
	def getProducts(self):
		url = self.endpointURL + '/products'
		r = requests.get(url)
		return json.loads(r.text)

	def getProductOrderBook(self, productID, level='1'):
		if int(level) < 0 or int(level) > 3:
			raise ValueError('Invalid level')
		url = self.endpointURL + '/products/{}/book'.format(productID)
		parameters = {'level': level}
		r = requests.get(url, params=parameters)
		return json.loads(r.text)
	
	'''
	{'trade_id': x, 'price': 'x', 'size': 'x', 'bid': 'x', 'ask': 'x', 'volume':'x', 'time':'x'}
	'''
	def getTicker(self, productID):
		url = self.endpointURL + '/products/{}/ticker'.format(productID)
		r = requests.get(url)
		return json.loads(r.text)

	'''
	[ {'time': 'x', 'trade_id': x, 'price': 'x', 'size': 'x', 'side': 'x'}, ... ]
	'''
	def getLatestTrades(self, productID):
		url = self.endpointURL + '/products/{}/trades'.format(productID)
		r = requests.get(url)
		return json.loads(r.text)

	'''
	[ [time, low, high, open, close, volume], ... ]
	'''
	def getHistoricRates(self, productID, granularity, start=None, end=None):
		if granularity not in {'60', '300', '900', '3600', '21600', '86400'}:
			raise ValueError('Invalid granularity')
		url = self.endpointURL + '/products/{}/candles'.format(productID)
		parameters = {'granularity': granularity}
		if start: parameters['start'] = start
		if end: parameters['end'] = end
		r = requests.get(url, params=parameters)
		return json.loads(r.text)
	
	'''
	{ 'open': 'x', 'high': 'x', 'low': 'x', 'volume': 'x' }
	'''
	def get24HourStats(self, productID):
		url = self.endpointURL + '/product/{}/statds'.format(productID)
		r = requests.get(url)
		return json.loads(r.text)
