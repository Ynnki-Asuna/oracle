#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import logging

import web3
import Config
import Trans
import Slack
from gate import GateAPI
from decimal import Decimal

logger = logging.getLogger(__name__)
logging.basicConfig(filename = 'log/oracle.log', level = logging.INFO)

class Oracle:
    def __init__(self):
        config = Config.Config()
        chain = config.getChain()
        oracle = config.getOracle()
        self.oracleAddr = oracle['address']
        self.w3 = web3.Web3(web3.HTTPProvider(chain['rpc']))
        filePath = os.path.join(os.getcwd(), 'data/tokens.json')
        with open(filePath) as json_file:
            self.tokenList = json.loads(json_file.read())

    def getOracle(self):
        oracleAddr = self.w3.toChecksumAddress(self.oracleAddr)
        abiFile = os.path.join(os.getcwd(), 'abi/Oracle.json')
        with open(abiFile) as json_file:
            abiJson = json.loads(json_file.read())
        # 获取ABI
        contract_abi = abiJson['abi']
        # 返回合约
        return self.w3.eth.contract(abi = contract_abi, address = oracleAddr)

    def update(self):
        for tokenObj in self.tokenList:
            try:
                pair = tokenObj['pair']
                gateIo = GateAPI.GateIO()
                ticker = gateIo.ticker(pair)
                price = Decimal(ticker['last']) * Decimal(1e18)
                self.updatePrice(tokenObj['symbol'], int(price))
                logger.info('The current price of {} has been set, and the price is {}'.format(tokenObj['symbol'], ticker['last']))
            except Exception as ex:
                Slack.Slack().sendNotify(tokenObj['symbol'])
                logger.error('update==> pair: {}, error: {}'.format(pair, ex))
        

    def updatePrice(self, symbol, price):
        gasPrice = self.w3.eth.gasPrice
        txnDict = self.getOracle().functions.updatePrice(symbol, price).buildTransaction({
                'gas': 100000,
                'gasPrice': gasPrice,
            })
        Trans.Trans().sendTransaction(txnDict)