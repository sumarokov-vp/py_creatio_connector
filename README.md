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
from os import getenv

def test_get_contact_leads_v4():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export SL_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    parameters = [
        "filter=Contact eq 'Marady Esther'"
    ]
    collection = cr.get_object_collection(
        object_name='Lead',
        parameters= parameters,
    )
    assert len(collection) == 0

test_get_contact_leads_v4()


```
## General documentation

### Types

        `ODATA_version` - Enumerator for different ODATA protocol versions

### Methods

#### "Creatio" class constructor

#### get_object


