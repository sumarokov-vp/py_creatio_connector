from sl_creatio_connector.creatio import ODATA_version, Creatio
import pytest
from os import getenv

def get_leads(cr: Creatio):
    cr.get_object(
        object_name='Lead',
        field='Contact',
        value='Marady Esther',
        order_by='Contact',
    )

def test_create_class():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    get_leads(cr=cr)

    cr = Creatio(
        creatio_host='http://crm.monusluy.com',
        login='Supervisor',
        password='CAMBO_CREATIO_PASS',  # export CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v3
    )
    get_leads(cr=cr)

if __name__ == '__main__':
    test_create_class()
