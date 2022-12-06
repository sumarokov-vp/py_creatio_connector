# <p align="center">Simple logic's Creatio ODATA connector</p>
<p align="center">Connector to integrate <a href="https://academy.creatio.com/docs/developer/integrations_and_api/data_services/odata/overview">Creatio ODATA API</a>.</p>

## Getting started

This connector tested for ODATA3 and ODATA4 protocols (including .net core version)

```
$ pip install sl_creatio_connector
```

## Using connector

```python
from creatio import Creatio

def get_leads():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    cr.get_object(
        object_name='Lead',
        field='Contact',
        value='Marady Esther',
        order_by='Contact',
    )


if __name__ == '__main__':
    get_leads()

```