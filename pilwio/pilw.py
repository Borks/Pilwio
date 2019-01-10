#!/usr/bin/env python
"""Pilw.io API python wrapper"""

import requests
import pilwio.v1 as v1

__author__ = "Borka Martin Orlov"
__version__ = "0.2.0"
__maintainer__ = "Borka Martin Orlov"
__email__ = "borka.orlov@fieldforce.com"
__status__ = "Development"

class V1(object):
    """Pilw.io API v1 python wrapper
    
    Arguments:
        apikey {String} -- API key
    """

    ENDPOINT = 'https://app.pilw.io:8443/v1'

    def __init__(self, apikey):
        self.apikey = apikey
        self.__init_submodules(apikey)
        

    def __init_submodules(self, apikey):
        self.vm = v1.VM(apikey, self.ENDPOINT)
        self.replica = v1.Replica(apikey, self.ENDPOINT)
        self.token = v1.Token(apikey, self.ENDPOINT)
        self.billing = v1.Billing(apikey, self.ENDPOINT)
        self.invoice = v1.Invoice(apikey, self.ENDPOINT)
        self.billing_account = v1.BillingAccount(apikey, self.ENDPOINT)
        self.card = v1.Card(apikey, self.ENDPOINT)
        self.storage = v1.Storage(apikey, self.ENDPOINT)


    def whoami(self):
        """Info about the user
        
        Returns:
            JSON -- Json object representation of the active user
        """
        response = requests.get(self.ENDPOINT + '/user-resource/user', headers={'apikey':self.apikey})

        return response.json()


    def set_apikey(self, apikey):
        """Set a new API key
        
        Arguments:
            apikey {String} -- API key
        """
        self.apikey = apikey
        self.__init_submodules(apikey)
