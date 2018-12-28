#!/usr/bin/env python3


from ClientProtocol import *
from Client import *

if __name__ == '__main__':

	webSocketFeedUrl = 'wss://ws-feed.pro.coinbase.com'

	client = Client(ClientProtocol, webSocketFeedUrl)

	client.startClient()
