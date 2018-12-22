import requests

class Billing:
    """Billing
    
    Arguments:
        apikey {String} -- Api key
        endpoint {String} -- Main api endpoint
    """


    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/user-resource'
        self.headers = {"apikey": apikey}

    
    def index(self, id): 
        """List billing account resources
        
        Arguments:
            id {String} -- Billing account id
        
        Returns:
            Json -- Json Array of resources
        """
        data = {'id': id}
        response = requests.get(self.endpoint + '/billing_resources', headers=self.headers, data=data)

        return response.json()


    def info(self, uuid):
        """Get resource billing info
        
        Arguments:
            uuid {String} -- Resource uuid
        
        Returns:
            Json -- Server Json response
        """ 
        params = {'uuid': uuid}
        response = requests.get(self.endpoint + '/resource_billing', headers=self.headers, params=params)

        return response.json()


    def update(self, uuid, id):
        """Associate resource with billing account
        
        Arguments:
            id {Integer} -- Billing account id
            uuid {String} -- Resource UUID
        """
        data = {'billing_account_id': id, 'uuid': uuid}
        response = requests.post(self.endpoint + '/resource_billing', headers=self.headers, data=data)

        return response.json()