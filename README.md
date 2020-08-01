# Pilw.io API wrapper.
Python wrapper for [Pilw.io API](https://developers.pilw.io/documentation/)

---

# Installation
```pip install pilwio-api```

---

## Usage

```python
import pilwio

""" Initialize version wrapper with apikey """
api = pilwio.V1('apikey')

""" Set new apikey if necessary """
api.set_apikey('new_api_key')

""" User info """
api.whoami()

```

---

### Virtual machines

```python
api.vm.index()

api.vm.show(uuid)

api.vm.create(vm)
api.vm.delete(uuid)
api.vm.update(uuid, **kwargs)
api.vm.start(uuid)
api.vm.stop(uuid)

api.vm.ips(uuid)
api.vm.reserve_ip(uuid)
api.vm.release_ip(uuid)

api.vm.clone(uuid, name)
api.vm.toggle_backup(uuid)
api.vm.rebuild(uuid, replica_uuid)
```

---

### Floating IP

```python
api.network.create(**kwargs)
api.network.list()
api.network.get(ipv4)
api.network.update(ipv4, **kwargs)
api.network.delete(ipv4)
api.network.assign(ipv4,uuid)
api.network.unassign(ipv4)
```
---

### Replicas
```python
api.replica.index(uuid, *rtype)
api.replica.create(uuid, *rtype)
api.replica.delete(uuid)
```

---

### Tokens
```python
api.token.index()
api.token.delete(token_id)
api.token.update(token_id, **kwargs)
api.token.create(token)
```

---

### Resource Billing
```python
api.billing.index(id)
api.billing.info(uuid)
api.billing.update(uuid, id)
```

---

### Credit cards
```python
api.card.index(account_id)
api.card.delete(card_id)
api.card.show(card_id)
api.card.set_primary(card_id)
```

---

### Invoices
```python
api.invoice.index(id)
api.invoice.show(invoice_id)
api.invoice.pay_all(account_id)
api.invoice.pay_amount(account_id, amount)
api.invoice.pay_invoice(invoice_id)
```

---

### Billing Accounts
```python
api.billing_account.index()
api.billing_account.show(account_id)
api.billing_account.update(account_id, account_data)
api.billing_account.set_default(account_id)
api.billing_account.get_unpaid(account_id)
```

---

### Storage
```
api.storage.url()
api.storage.show(name)
api.storage.index(billing_account_id) #param optional
api.storage.user()
api.storage.keys()
api.storage.delete_key(key)
api.storage.create_key()
```
