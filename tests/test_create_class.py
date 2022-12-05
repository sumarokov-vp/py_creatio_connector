from creatio import ODATA_version, Creatio
import pytest

def test_create_class():
    cr = Creatio(
        creatio_host= 'http://creatio.simplelogic.ru:5000',
        login = 'Vova',
        password= '9#zgr@ci6!bveH',
        odata_version= ODATA_version.v4core
    )
    assert(cr.receipt_tasks_count('904aba88-bea9-4425-8bdd-b1584ffb0d63') == 1)