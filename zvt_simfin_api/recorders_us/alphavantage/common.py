# -*- coding: utf-8 -*-
import logging

import requests
import io
import pandas as pd

logger = logging.getLogger(__name__)


class ApiWrapper(object):

    api_key = '' # api key for alphavantage
    base_url = 'https://www.alphavantage.co/query'

    def generate_request_param(self, params):
        param = {}
        if params and type(params)==dict:
            param.update(params)
        param.update({'apikey': self.api_key})
        return param
          
    def request(self, **kwargs):
        param = self.generate_request_param(kwargs)
        resp = requests.get(self.base_url, params=param)
        return resp



    
            


