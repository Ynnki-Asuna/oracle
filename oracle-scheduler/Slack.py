#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import Config
import requests

class Slack:

    def __init__(self):
        config = Config.Config()
        slack = config.getSlack()
        self.apiUrl = slack['apiUrl']

    def sendNotify(self, symbol):
        content = 'Oracle-symbol: {} There is an exception when setting the price, please check the log in time.'.format(symbol)
        self.sendToSlack(content)

    def sendToSlack(self, content):
        headers = {"Content-Type": "application/json"}
        message = {
            'text': content
        }
        response = requests.post(url=self.apiUrl, headers=headers, data=json.dumps(message), timeout=100)
        try:
            if not str(response.status_code).startswith('2'):
                return {
                    "success": False,
                    "code": response.status_code,
                    "msg": "server error {}".format(response.text)
                }
        except BaseException as e:
            print("%s , %s" % (self.apiUrl, e))
            return {"success": False, "code": -1, "msg": e}