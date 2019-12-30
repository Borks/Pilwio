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


    def index(self, uuid, *rtype):
        """List replicas of a VM

        Arguments:
            uuid {String} -- Identifier of VM
            rtype {String} -- replica type ("backup", "snapshot")

            Default replica type is "snapshot".

        Returns:
            Json -- Json array of replicas
        """
        ALLOWED_RYTPE_VALUES = ["backup", "snapshot"]
        params = {'uuid': uuid}

        for value in rtype:
            if value in ALLOWED_RYTPE_VALUES:
                params['r_type'] = value

        response = requests.get(self.endpoint, headers=self.headers, params=params)

        return response.json()


    def create(self, uuid, *rtype):
        """Create a new replica

        Arguments:
            uuid {String} -- VM identifier
            rtype {String} -- replica type ("backup", "snapshot")

            Default replica type is "snapshot".

        Returns:
            Json -- Replica info
        """
        ALLOWED_RYTPE_VALUES = ["backup", "snapshot"]
        data = {'uuid': uuid}

        for value in rtype:
            if value in ALLOWED_RYTPE_VALUES:
                data['r_type'] = value

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
