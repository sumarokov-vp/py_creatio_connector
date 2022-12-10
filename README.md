# <p align="center">Simple logic's Creatio ODATA connector</p>
<p align="center">Connector to integrate <a href="https://academy.creatio.com/docs/developer/integrations_and_api/data_services/odata/overview">Creatio ODATA API</a>.</p>
<p><a href="https://documenter.getpostman.com/view/10204500/SztHX5Qb">Creatio ODATA API postman documentation</a></p>

## Getting started

This connector tested for ODATA3 and ODATA4 protocols (including .net core version)

```
$ pip install sl_creatio_connector
```

## Quick start

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

def create_lead():
    creatio = Creatio(
        creatio_host= CREATIO_HOST,
        login= CREATIO_LOGIN,
        password= CREATIO_PASS,
        odata_version= ODATA_version.v3
    )

    dict_data = {
        'Contact': cu.name,
        'MobilePhone': cu.mobile_phone,
        'RegisterMethodId': db_worker.get_setting('new_lead_register_method'),
        'CountryId': db_worker.get_setting('creatio_country_id'),
        'QualifyStatusId': db_worker.get_setting('new_lead_stage'),
        'UsrActivityResultId': db_worker.get_setting('new_lead_activity_result'),
        'UsrMoneyAmount': cu.lead_amount,
        'UsrTerm':str(cu.lead_term),
    }
    lead = creatio.create_object('Lead', dict_data)



if __name__ == '__main__':
    get_leads()

```
## General documentation

### Types

        `ODATA_version` - Enumerator for different ODATA protocol versions

### Methods

#### "Creatio" class constructor

#### get_object


