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


    def update(self, uuid, name=False, ram=False, vcpu=False): 
        """Update virtual machine
        
        Arguments:
            uuid {String} -- UUID of vm to change
        
        Keyword Arguments:
            name {String} -- New VM name (default: {False})
            ram {Integer} -- VM ram (default: {False})
            vcpu {Integer} -- VM vCPU count (default: {False})
        
        Returns:
            Json -- Server json response
        """
        data = { 'uuid': uuid }

        if name: data['name'] = name
        if ram: data['ram'] = ram
        if vcpu: data['vcpu'] = vcpu

        response = requests.patch(self.endpoint, headers=self.headers, data=data)

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


    def ips(self, uuid):
        """Get virtual machine IPs
        
        Arguments:
            uuid {String} -- VM uuid
        
        Returns:
            Json -- Server json response
        """
        params = {'uuid': uuid}
        response = requests.get(self.endpoint + '/ip', headers=self.headers, params=params)

        return response.json()


    def release_ip(self, uuid):
        """Release a virtual machine's public IP address. 
        The address is not reserved, it may be assigned to some other virtual machine at a later time.
        
        Arguments:
            uuid {String} -- VM uuid
        
        Returns:
            Json -- Server json response
        """
        data = {'uuid': uuid}
        response = requests.delete(self.endpoint + '/ip/public', headers=self.headers, data=data)

        return response.json()


    def reserve_ip(self, uuid):
        """Reserve and assign a public IP address for a virtual machine.
        
        Arguments:
            uuid {String} -- VM uuid
        
        Returns:
            Json -- Server jsoon response
        """
        data = {'uuid': uuid}
        response = requests.post(self.endpoint + '/ip/public', headers=self.headers, data=data)

        return response.json()


    def toggle_backup(self, uuid):
        """Toggle automatic backups on a VM
        
        Arguments:
            uuid {String} -- UUID
        
        Returns:
            JSON -- Json response from server
        """
        data = { 'uuid': uuid }
        response = requests.post( self.endpoint + '/backup', headers=self.headers, data=data ) 

        return response.json()

    
    def clone(self, uuid, name):
        """Close a VM
        
        Arguments:
            uuid {String} -- Vm UUID to clode
            name {String} -- New VM name
        
        Returns:
            Json -- Json response from server
        """
        data = { 'uuid': uuid, 'name': name }
        response = requests.post( self.endpoint + '/clone', headers=self.headers, data=data ) 

        return response.json()

    
    def rebuild(self, uuid, replica_uuid):
        """Rebuild a VM from a replica
        
        Arguments:
            uuid {String} -- VM identifier
            replica_uuid {String} -- Replica identifier
        
        Returns:
            Json -- Json response from server
        """
        data = {'replica_uuid': replica_uuid, 'uuid': uuid}
        response = requests.post(self.endpoint + '/rebuild', headers=self.headers, data=data)
        
        return response.json()
        