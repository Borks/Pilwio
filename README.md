# Pilw.io API Python wrapper.

## Python Requirements
> requests

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
api.vm.start(uuid)
api.vm.stop(uuid)

api.vm.clone(uuid, name)
api.vm.toggle_backup(uuid)
api.vm.rebuild(uuid, replica_uuid)
```

---

### Replicas
```python
api.replica.index(uuid)
api.replica.create(uuid)
api.replica.delete(uuid)
```

---

### Tokens
```python
api.token.index()
api.token.delete(token_id)
api.token.update(token_id, description, restricted, billing_account_id)
api.token.create(token)
```

---

### Billing
```
api.billing.index(id)
api.billing.info(uuid)
api.billing.update(uuid, id)