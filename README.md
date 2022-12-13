# <p align="center">Simple logic's Creatio ODATA connector</p>
<p align="center">Connector to integrate <a href="https://academy.creatio.com/docs/developer/integrations_and_api/data_services/odata/overview">Creatio ODATA API</a>.</p>
<p><a href="https://documenter.getpostman.com/view/10204500/SztHX5Qb">Creatio ODATA API postman documentation</a></p>

## Getting started

This connector tested for ODATA3 and ODATA4 protocols (including .net core version)

```bash
$ pip install sl_creatio_connector
```

```python

from sl_creatio_connector.creatio import Creatio
from sl_creatio_connector.constants import ODATA_version

# get collection
def get_contact_leads():
    cr = Creatio(
        creatio_host='http://creatio.mydomen.com:5000',
        login='Supervisor',
        password='Supervisor',
        odata_version=ODATA_version.v4core
    )
    parameters = [
        "filter=Contact eq 'Marady Esther'"
    ]
    collection = cr.get_object_collection(
        object_name= 'Lead',
        parameters= parameters,
    )
    assert len(collection) == 0

def create_and_delete_contact():
    cr = Creatio(
        creatio_host='http://creatio.mydomen.com:5000',
        login='Supervisor',
        password='Supervisor',
        odata_version=ODATA_version.v4core
    )
    data = {
        'Name': "Test name"
    }
    created_contact = cr.create_object(
        object_name= 'Contact',
        data= data,
    )
    created_id = created_contact['Id']
    status_code = cr.delete_object('Contact', created_id).status_code

def get_contact_by_id():
    cr = Creatio(
        creatio_host='http://creatio.mydomen.com:5000',
        login='Supervisor',
        password='Supervisor',
        odata_version=ODATA_version.v4core
    )
    contact_dict = cr.get_contact_by_id('b2a8c568-002f-4fd1-a15a-ffda98f5f63b')
```


