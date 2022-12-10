from constants import ODATA_version
from creatio import Creatio
import pytest
from os import getenv


def test_create_class_v4():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export SL_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    cr.get_object(
        object_name='Lead',
        field='Contact',
        value='Marady Esther',
        order_by='Contact',
    )

def test_create_class_v3():
    cr = Creatio(
        creatio_host='http://crm.monusluy.com',
        login='Supervisor',
        password=getenv('CAMBO_CREATIO_PASS'),  # export CAMBO_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v3
    )
    cr.get_object(
        object_name='Lead',
        field='Contact',
        value='Marady Esther',
        order_by='Contact',
    )

def test_get_contact_by_id_v4():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export SL_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    cr.get_contact_by_id('b10e4cef-66d6-46ce-9479-83a125c750ae')

def test_get_contact_by_id_v3():
    cr = Creatio(
        creatio_host='http://crm.monusluy.com',
        login='Supervisor',
        password=getenv('CAMBO_CREATIO_PASS'),  # export CAMBO_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v3
    )
    cr.get_contact_by_id('b2a8c568-002f-4fd1-a15a-ffda98f5f63b')

if __name__ == '__main__':
    test_get_contact_by_id_v3()
