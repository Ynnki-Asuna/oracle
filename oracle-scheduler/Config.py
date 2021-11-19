#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('properties.conf')
    
    def getWallet(self):
        return self.config['wallet']

    def getGate(self):
        return self.config['gate']

    def getChain(self):
        return self.config['chain']
    
    def getOracle(self):
        return self.config['oracle']
