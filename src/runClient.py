#!/usr/bin/env python3


from WebSocketClientProtocol import *
from Client import *

if __name__ == '__main__':

	webSocketFeedUrl = 'wss://ws-feed.pro.coinbase.com'

	client = Client(WebSocketClientProtocol, webSocketFeedUrl)

	client.startClient()
