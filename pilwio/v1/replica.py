import requests

class Replica:
    """Resource replica management 
    
    Arguments:
        apikey {String} -- User API key
        endpoint {String} -- Main API endpoint
    """


    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/user-resource/vm/replica'
        self.headers = {"apikey": apikey}


    def index(self, uuid):
        """List replicas of a VM
        
        Arguments:
            uuid {String} -- Identifier of VM

        Returns:
            Json -- Json array of replicas
        """
        params = {'uuid': uuid}
        response = requests.get(self.endpoint, headers=self.headers, params=params)

        return response.json()


    def create(self, uuid):
        """Create a new replica
        
        Arguments:
            uuid {String} -- VM identifier
        
        Returns:
            Json -- Replica info
        """
        data = {'uuid': uuid}
        response = requests.post(self.endpoint, headers=self.headers, data=data)

        return response.json()


    def delete(self, uuid):
        """Delete a replica
        
        Arguments:
            uuid {String} -- Replica UUID
        
        Returns:
            Json -- Json response from server
        """
        data = {'replica_uuid': uuid}
        response = requests.delete(self.endpoint, headers=self.headers, data=data)

        return response.json()

    