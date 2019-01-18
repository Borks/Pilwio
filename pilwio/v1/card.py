import requests

class Card:
    """Credit card management
    
    Arguments:
        apikey {[type]} -- [description]
        endpoint {[type]} -- [description]
    """
    
    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/payment/card'
        self.headers = {"apikey": apikey}

    
    def index(self, account_id):
        """Credit cards attached to billing account
        
        Arguments:
            account_id {Integer} -- Billing account ID
        
        Returns:
            Json -- Server Json response
        """
        params = {'billing_account_id': account_id}
        response = requests.get(self.endpoint + '/list', headers=self.headers, params=params)

        return response.json()


    def show(self, card_id):
        """Credit card details
        
        Arguments:
            card_id {Integer} -- Credit card ID
        
        Returns:
            Json -- Server Json response
        """
        params = {'payment_object_id': card_id}
        response = requests.get(self.endpoint, headers=self.headers, params=params)

        return response.json()


    def delete(self, card_id):
        """Remove a credit card 
        
        Arguments:
            card_id {Integer} -- Credit card ID
        
        Returns:
            Json -- Server Json response
        """
        params = {'payment_object_id': card_id}
        response = requests.delete(self.endpoint, headers=self.headers, params=params)

        return response.json()

    
    def set_primary(self, card_id):
        """Set a credit card as primary for billing account
        
        Arguments:
            card_id {Integer} -- Card ID

        Returns:
            Json -- Server Json Response
        """
        data = {'payment_object_id': card_id}
        response = requests.put(self.endpoint + '/set_primary', headers=self.headers, data=data)
    
        return response.json()
    