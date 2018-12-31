import pytest
from RESTfulClient import *

class TestRESTfulClient():
	
	def test_getProducts(self):
		restfulClient = RESTfulClient()
		assert restfulClient.getProducts().status_code == 200

	def test_getProductOrderBook(self):
		restfulClient = RESTfulClient()
		assert restfulClient.getProductOrderBook('BTC-USD', '1').status_code == 200
	
	def test_getTicker(self):
		restfulClient = RESTfulClient()
		assert restfulClient.getTicker('BTC-USD').status_code == 200

	def test_getLatestTrades(self):
		restfulClient = RESTfulClient()
		assert restfulClient.getLatestTrades('BTC-USD').status_code == 200
	
	def test_getHistoricRates(self):
		restfulClient = RESTfulClient()
		assert restfulClient.getHistoricRates('BTC-USD', 60).status_code == 200
	
	def test_get24HourStats(self):
		restfulClient = RESTfulClient()
		assert restfulClient.get24HourStats('BTC-USD').status_code == 200
