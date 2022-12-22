from sl_creatio_connector import ODATA_version, Creatio
import pytest
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

def test_get_contact_leads_v3():
    cr = Creatio(
        creatio_host='http://crm.monusluy.com',
        login='Supervisor',
        password=getenv('CAMBO_CREATIO_PASS'),  # export CAMBO_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v3
    )
    parameters = [
        "filter=Contact eq 'Marady Esther'"
    ]
    collection = cr.get_object_collection(
        object_name='Lead',
        parameters= parameters,
    )
    assert len(collection) == 2

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

def test_create_and_delete_contact_by_id_v3():
    cr = Creatio(
        creatio_host='http://creatio.simplelogic.ru:5000',
        login='Vova',
        password=getenv('SL_CREATIO_PASS'),  # export SL_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v4core
    )
    data = {
        'Name': "Test name"
    }
    created_contact = cr.create_object(
        'Contact',
        data= data,
    )
    created_id = created_contact['Id']
    status_code = cr.delete_object('Contact', created_id).status_code
    assert status_code == 204

def test_create_and_delete_contact_by_id_v4():
    cr = Creatio(
        creatio_host='http://crm.monusluy.com',
        login='Supervisor',
        password=getenv('CAMBO_CREATIO_PASS'),  # export CAMBO_CREATIO_PASS="my_massword"
        odata_version=ODATA_version.v3
    )
    data = {
        'Name': "Test name"
    }
    created_contact = cr.create_object(
        'Contact',
        data= data,
    )
    created_id = created_contact['Id']
    # status_code = cr.delete_object('Contact', created_id).status_code
    # assert status_code == 204

if __name__ == '__main__':
    test_get_contact_leads_v4()
    test_get_contact_leads_v3()
    test_get_contact_by_id_v3()
    test_get_contact_by_id_v4()
    test_create_and_delete_contact_by_id_v3()
    test_create_and_delete_contact_by_id_v4()