#!/usr/bin/env python3

import requests
import json
import datetime

class RESTfulClient():

	def __init__(self):
		self.endpointURL = 'https://api.pro.coinbase.com'
	
	# Start time and end time must be in ISO 8601 format
	def getHistoricRates(self, productID, granularity, start=None, end=None):
		if granularity not in {60, 300, 900, 3600, 21600, 86400}:
			raise ValueError('Invalid granularity')
		url = self.endpointURL + '/products/{}/candles'.format(productID)
		parameters = {'granularity': granularity}
		if start: parameters['start'] = start
		if end: parameters['end'] = end
		r = requests.get(url, data=json.dumps(parameters))
		for bucket in json.loads(r.text):
			print('Closing price: {}'.format(bucket[4]))

restfulClient = RESTfulClient()

restfulClient.getHistoricRates('BTC-USD', 21600, 2018-12-29, 2018-12-30)
