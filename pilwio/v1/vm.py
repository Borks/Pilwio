import requests

class VM:
    """Virtual machine management
    
    Arguments:
        object {Class} -- Obj
    """
    

    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/user-resource/vm'
        self.headers = {"apikey": apikey}


    def index(self):
        """List virtual machines
        
        Returns:
            Array -- Array of VM descriptions
        """
        response = requests.get(self.endpoint + '/list', headers=self.headers)

        return response.json()


    def show(self, uuid):
        """Get single VM info
        
        Arguments:
            uuid {String} -- Unique identifier
        
        Returns:
            Json -- Response from server
        """
        params = {'uuid': uuid}
        response = requests.get(self.endpoint, headers=self.headers, params=params)

        return response.json()

    def create(self, vm):
        """Create a new vm
        
        Arguments:
            vm {Object} -- Object describing VM
        
        TODO:
            Validate vm attributes according to requirements from /parameters
            Current api returns an 'unconvenient' array of params though
        """
        data = vm
        response = requests.post( self.endpoint, headers=self.headers, data=data ) 

        return response.json()


    def delete(self, uuid):
        """Delete a virtual machine
        
        Arguments:
            uuid {String} -- VM unique identifier
        
        Returns:
            Json -- Response from server
        """
        data = { 'uuid': uuid }
        response = requests.delete( self.endpoint, headers=self.headers, data=data ) 

        return response.json()

    
    def start(self, uuid):
        """Start a VM
        
        Arguments:
            uuid {String} -- VM identifier
        
        Returns:
            Json -- Server Json reponse
        """
        data = { 'uuid': uuid }
        response = requests.post( self.endpoint + '/start', headers=self.headers, data=data ) 

        return response.json()


    def stop(self, uuid):
        """Stop a VM
        
        Arguments:
            uuid {String} -- VM identifier
        
        Returns:
            Json -- Server Json response
        """
        data = { 'uuid': uuid }
        response = requests.post( self.endpoint + '/stop', headers=self.headers, data=data ) 

        return response.json()


    def toggle_backup(self, uuid):
        data = { 'uuid': uuid }
        response = requests.post( self.endpoint + '/backup', headers=self.headers, data=data ) 

        return response.json()

    
    def clone(self, uuid, name):
        data = { 'uuid': uuid, 'name': name }
        response = requests.post( self.endpoint + '/clone', headers=self.headers, data=data ) 

        return response.json()

        