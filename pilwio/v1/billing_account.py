import requests

class BillingAccount:
    """Virtual machine management
    
    Arguments:
        object {Class} -- Obj
    """
    

    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/payment/billing_account'
        self.headers = {"apikey": apikey}
    

    def index(self):
        """List billing accounts
        
        Returns:
            Json -- Server Json response
        """
        response = requests.get(self.endpoint + '/list', headers=self.headers)

        return response.json()

    
    def show(self, account_id):
        """Billing account details
        
        Arguments:
            account_id {Integer} -- Billing account id
        
        Returns:
            Json -- Server Json response
        """
        params = {'billing_account_id': account_id}
        response = requests.get(self.endpoint, headers=self.headers, params=params)
        
        return response.json()

    
    def update(self, account_id, account_data):
        """Update billing account's data. 
        All existing data fields that billing account already has, must be passed along also. 
        Otherwise this data will be deleted (PS! e-mail field can't be deleted).
        
        Arguments:
            account_id {Integer} -- Billing Account ID
            account_data {Dict} -- Billing account repr in dict form

        Response:
            Json -- Server Json response
        """
        account_data['billing_account_id'] = account_id
        response = requests.put(self.endpoint, headers=self.headers, data=account_data)

        return response.json()

    
    def set_default(self, account_id):
        """Set billing account as default
        
        Arguments:
            account_id {Integer} -- Billing account ID
        
        Returns:
            Json -- Server Json response
        """
        data = {'billing_account_id': account_id}
        response = requests.post(self.endpoint + '/set_default', headers=self.headers, data=data)

        return response.json()

    
    def get_unpaid(self, account_id):
        """Get billing account's unpaid total amount (with VAT included). 
        This is unpaid amount of all invoices who's status is not 'paid'.
        
        Arguments:
            account_id {Integer} -- Billing account ID
        
        Returns:
            Json -- Server Json Response
        """
        params = {'billing_account_id': account_id}
        response = requests.post(self.endpoint + '/set_default', headers=self.headers, params=params)

        return response.json()