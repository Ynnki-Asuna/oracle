#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Provide the GateIO class to abstract web interaction
'''

import sys
sys.path.append('..')
from gate.HttpUtil import httpGet
import Config

class GateIO:
    def __init__(self):
        config = Config.Config()
        gate = config.getGate()
        self.__url = gate['apiUrl']

    ## General methods that query the exchange

    #单项交易行情
    def ticker(self, param):
        URL = "/api2/1/ticker"
        return httpGet(self.__url, URL, param)