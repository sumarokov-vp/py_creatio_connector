CREATIO_URL = 'http://crm.dragonmoney.vn'
ODATA_VERSION = 3

from django.test import TestCase

# Create your tests here.
from creatio import Creatio

class TestCreatio(TestCase):
    def setUp(self):
        self.creatio: Creatio

    #@skip("Don't want to test")
    def test_create_lead(self):
        self.creatio = Creatio(
            creatio_host= 'http://crm.monusluy.com',
            login= 'Supervisor',
            password= '***',
            odata_version= '3',
        )

        lead_id = self.creatio.post_lead(
            register_method= 'BA097C3A-31CF-48A7-A196-84FAD50EFE8D',
            country= 'A6A5593A-12C9-4B60-8573-A105C1A2CD77',
            lead_stage= 'd790a45d-03ff-4ddb-9dea-8087722c582c',
            activity_result= 'a68b44b3-a2c4-4252-bd93-28d0160a58f7',
            full_name= 'TEST.PY',
            mobile_phone = '+855 99 999 999',
            amount= '100',
            term= '15',
        )

        self.assertEqual(len(lead_id), 36)