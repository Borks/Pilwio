import requests

class Storage:

    def __init__(self, apikey, endpoint):
        """Pilw.io S3 storage api
        
        Arguments:
            apikey {String} -- Api key
            endpoint {String} -- PilwIO api endpoint
        """
        self.apikey = apikey
        self.endpoint = endpoint + '/storage'
        self.headers = {"apikey": apikey}

    
    def url(self):
        """GET S3 Api url
        
        Returns:
            Json -- Server json response
        """
        response = requests.get(self.endpoint + '/api/s3', headers=self.headers)

        return response.json()


    def show(self, name):
        """Get bucket information
        
        Arguments:
            name {String} -- S3 bucket name
        
        Returns:
            Json -- Server json response
        """
        params = {'name': name}
        response = requests.get(self.endpoint + '/bucket', headers=self.headers, params=params)

        return response.json()


    def index(self, billing_account_id=False):
        """List user's buckets. Optionally filter the list by billing account.


        
        Keyword Arguments:
            billing_account_id {Integer} -- Filter buckets by billing account (default: {False})
        
        Returns:
            Json -- Server json response
        """
        params = {}
        if billing_account_id:
            params['billing_account_id'] = billing_account_id

        response = requests.get(self.endpoint + '/bucket/list', headers=self.headers, params=params)

        return response.json()

    
    def user(self):
        """Get S3 user info, including their access and secret keys. User and keys will be generated, 
        if they do not exist already.
        
        Returns:
            Json -- Server json response
        """
        response = requests.get(self.endpoint + '/user', headers=self.headers)

        return response.json()
    

    def delete_key(self, access_key):
        """Delete an S3 key
        
        Arguments:
            access_key {String} -- Access Key
        
        Returns:
            Json -- Server json response
        """
        data = {'access_key': access_key}
        response = requests.delete(self.endpoint + '/user/keys', headers=self.headers, data=data)
        
        return response.json()

    
    def keys(self):
        """Get all user S3 keys 
        
        Returns:
            Json -- Json list of user keys
        """
        response = requests.get(self.endpoint + '/user/keys', headers=self.headers)

        return response.json()


    def create_key(self):
        """Generate a new S3 key pair.
        
        Returns:
            Json -- list of all keys.
        """
        response = requests.post(self.endpoint + '/user/keys', headers=self.headers)

        return response.json()