import requests
import json

class Network:
    """Floating IP management

    Arguments:
        object {Class} -- Obj
    """
    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/network'
        self.headers = {"apikey": apikey}

    def create(self, **kwargs):
        """Creates new floating IP

        Keyword Arguments:
            name {String} -- IP name (default: {False})
            billing_account_id {Integer} -- Billing account id (default: {False})

        Returns:
            Array -- Array of the newly created Floating IP
        """

        ALLOWED_KWARGS = ['name', 'billing_account_id']
        data = {}

        for key, value in kwargs.items():
            if key in ALLOWED_KWARGS:
                data[key] = value
        data1 = json.dumps(data)
        hdrs = self.headers
        hdrs['Content-Type'] = 'application/json'
        response = requests.post(self.endpoint + '/ip_addresses', headers=hdrs, data = data1)
        return response.json()

    def list(self):
        """List all Floating IP addresses

        Returns:
            Array -- Array of all IP addresses
        """
        response = requests.get(self.endpoint + '/ip_addresses', headers=self.headers)

        return response.json()

    def get(self,ipv4):
        """Get one machine's IP info using the public ipv4 address

        Arguments:
            ipv4 {String} -- Public ipv4 address

        Returns:
            Array -- Array of one machine's IP info
        """
        response = requests.get(self.endpoint + '/ip_addresses/' + ipv4, headers=self.headers)

        return response.json()

    def update(self,ipv4, **kwargs):
        """Updates a Floating IP

        Arguments:
            ipv4 {String} -- Public ipv4 address

        Keyword Arguments:
            name {String} -- IP name (default: {False})
            billing_account_id {Integer} -- Billing account id (default: {False})

        Returns:
            Array -- Array of the new Floating IP
        """

        ALLOWED_KWARGS = ['name', 'billing_account_id']
        data = {}

        for key, value in kwargs.items():
            if key in ALLOWED_KWARGS:
                data[key] = value
        data1 = json.dumps(data)
        hdrs = self.headers
        hdrs['Content-Type'] = 'application/json'
        response = requests.patch(self.endpoint + '/ip_addresses/' + ipv4, headers=hdrs, data=data1)

        return response.json()

    def delete(self,ipv4):
        """Deletes a floating IP address

        Arguments:
            ipv4 {String} -- Public ipv4 address

        Returns:
            Json -- Response from server
        """
        response = requests.delete(self.endpoint + '/ip_addresses/' + ipv4, headers=self.headers)

        return response.json()

    def assign(self,ipv4,uuid):
        """Deletes a floating IP address

        Arguments:
            ipv4 {String} -- Public ipv4 address
            uuid {String} -- UUID of the machine you wish to assign the IP to

        Returns:
            Json -- Response from server
        """

        data = { 'vm_uuid': uuid }
        data1 = json.dumps(data)
        hdrs = self.headers
        hdrs['Content-Type'] = 'application/json'
        response = requests.post(self.endpoint + '/ip_addresses/' + ipv4 + '/assign', headers=hdrs, data=data1)

        return response.json()

    def unassign(self,ipv4):
        """Deletes a floating IP address

        Arguments:
            ipv4 {String} -- Public ipv4 address

        Returns:
            Json -- Response from server
        """
        hdrs = self.headers
        hdrs['Content-Type'] = 'application/json'
        response = requests.post(self.endpoint + '/ip_addresses/' + ipv4 + '/unassign', headers=hdrs)

        return response.json()
