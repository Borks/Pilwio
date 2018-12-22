import requests

class Invoice:
    """invoice management
    
    Arguments:
        object {Class} -- Obj
    """
    

    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint + '/payment'
        self.headers = {"apikey": apikey}


    def index(self, billing_account_id):
        """List Billing account invoices
        
        Arguments:
            billing_account_id {Integer} -- Billing account id
        
        Returns:
            Json -- Server Json response
        """
        params = {'billing_account_id': billing_account_id}
        response = requests.get(self.endpoint + '/invoice/list', headers=self.headers, params=params)

        return response.json()


    def show(self, invoice_id):
        """Get invoice details
        
        Arguments:
            invoice_id {Integer} -- Invoice id
        
        Returns:
            Json -- Server Json response
        """
        params = {'invoice_id': invoice_id}
        response = requests.get(self.endpoint + '/invoice', headers=self.headers, params=params)

        return response.json()


    def pay_all(self, account_id):
        """Pay all billing account's unpaid invoices. Pays oldest invoices first.
        
        Arguments:
            account_id {Integer} -- Billing account ID
        
        Returns:
            Json -- Servers Json response
        """
        data = {'billing_account_id': account_id}
        response = requests.post(self.endpoint + '/pay_all', headers=self.headers, data=data)

        return response.json()


    def pay_amount(self, account_id, amount):
        """Pay the amount specified. Pays billing account's oldest unpaid invoices first.
        
        Arguments:
            account_id {Integer} -- Billing Account ID
            amount {Float} -- Amount to pay
        
        Returns:
            Json -- Json response from Server
        """
        data = {'billing_account_id': account_id, 'amount': amount}
        response = requests.post(self.endpoint + '/pay_amount', headers=self.headers, data=data)

        return response.json()


    def pay_invoice(self, invoice_id):
        """Pay invoice
        
        Arguments:
            invoice_id {Integer} -- Invoice ID
        
        Returns:
            Json -- Server Json response
        """
        data = {'invoice_id': invoice_id}
        response = requests.post(self.endpoint + '/pay_invoice', headers.self.headers, data=data)

        return response.json()
