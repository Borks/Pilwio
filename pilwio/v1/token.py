import requests

class Token:
    """User API token management

    Arguments:
        apikey {String} -- Api key
        endpoint {string} -- Main api endpoint
    """

    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/user-resource/token'
        self.headers = {"apikey": apikey}

    
    def index(self):
        """List api tokens
        
        Returns:
            Json -- Array of tokens
        """
        response = requests.get(self.endpoint + '/list', headers=self.headers)

        return response.json()

    
    def delete(self, token_id):
        """Delete an API token
        
        Arguments:
            token_id {Integer} -- Token id
        
        Returns:
            Json -- Server Json Response
        """
        data = {'token_id': token_id}
        response = requests.delete(self.endpoint, headers=self.headers, data=data)

        return response.json()

    
    def update(self, token_id, **kwargs):
        """Update an existing token
        
        Arguments:
            token_id {Integer} -- Token Id
        
        Keyword Arguments:
            description {String} -- Token Description
            restricted {Boolean} -- Token Rights
            billing_account_id {Integer} -- Billing account, that token is authorized to manage
        
        Returns:
            Json -- Json Response from Server
        """
        ALLOWED_KWARGS = ['description', 'restricted', 'billing_account_id']
        data = {'token_id': token_id}

        for key, value in kwargs:
            if key in ALLOWED_KWARGS:
                data[key] = value

        response = requests.patch(self.endpoint, headers=self.headers, data=data)

        return response.json()


    def create(self, token):
        """Create a new api token
        
        Arguments:
            token {Dict} -- Dictionary of token attributes
        
        Returns:
            Json -- Json Response from server
        """
        response = requests.post(self.endpoint, headers=self.headers, data=token)

        return response.json()