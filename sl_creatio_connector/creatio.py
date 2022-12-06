import json
import requests
from enum import Enum
from os import getenv


# CREATIO_URL = 'http://crm.dragonmoney.vn'
# ODATA_VERSION = 3


HEADERS_V3_TEMPLATE = {
    'Content-Type':'application/json;odata=verbose',
    'ForceUseSession':'true',
    'Accept':'application/json;odata=verbose',
    'BPMCSRF': '',
}

HEADERS_V4_TEMPLATE = {
    'Content-Type':'application/json; charset=utf-8',
    'ForceUseSession':'true',
    'Accept':'application/json; charset=utf-8',
    'BPMCSRF': '',
}

RECEIPT_OBJECT_NAME = 'SLReceipt'
TASK_OBJECT_NAME = 'SLReceiptTask'
DESK_OBJECT_NAME = 'SLTrelloDesks'
PHONE_BOOK_OBJECT_NAME = 'UsrPhoneBook'



        

class ODATA_version(Enum):
    v3= {
            'service_path': '/0/ServiceModel/EntityDataService.svc',
            'headers': HEADERS_V3_TEMPLATE,
        }
    v4= {
            'service_path': '/0/odata',
            'headers': HEADERS_V4_TEMPLATE,
        }
    v4core= {
            'service_path': '/odata',
            'headers': HEADERS_V4_TEMPLATE,
        }
    test = {
            'service_path': '/0/ServiceModel/EntityDataService.svc',
            'headers': 'test',
        }
    

class Creatio():
    def __init__(self, creatio_host, login, password, odata_version):
        self.creatio_url = creatio_host
        self.odata_version = odata_version
        self.odata_service_link = self.creatio_url + odata_version.value['service_path']
        self.headers = odata_version.value['headers']
        done, text = self.forms_auth(login, password)
        if done:
            self.headers['BPMCSRF'] = text['BPMCSRF']
            self.cookies = text
        else:
            raise Exception(text)

    def forms_auth(self, login, password):
        """ Аутентификация ODATA """
        url = f'{self.creatio_url}/ServiceModel/AuthService.svc/Login'
        dict_data = {
            "UserName": login,
            'UserPassword': password,
        }
        json_data = json.dumps(dict_data)
        response = requests.post(url=url, headers=self.headers, data= json_data)

        response_data = response.json()
        if response_data['Code'] == 0:
            return True, response.cookies
        else:
            return False, response_data['Message']

    def create_object(self, object_name, data):
        """ CREATE запрос в Creatio """
        if self.odata_version == ODATA_version.v3:
            url = self.odata_service_link + f"/{object_name}Collection"
        else:
            url = self.odata_service_link + f"/{object_name}"
        json_data = json.dumps(data)
        response = requests.post(
            url=url,
            headers=self.headers,
            data= json_data,
            cookies= self.cookies,
        )

        if self.odata_version == ODATA_version.v3:
            object = json.loads(response.content)['d']
        else:
            object = json.loads(response.content)

        return object


    def delete_object(self, object_name: str, object_id: str):
        """ DELETE запрос к Creatio """
        if self.odata_version == ODATA_version.v3:
            url = self.odata_service_link + f"/{object_name}Collection(guid'{object_id}')"
        else:
            url = self.odata_service_link + f"/{object_name}({object_id})"

        response = requests.delete(
            url=url,
            headers=self.headers,
            cookies= self.cookies,
        )
        return response.status_code

    def post_receipt(self, board_creatio_id):
        """ Создать экземпляр SLReceipt  в Creatio """
        dict_data = {
            'SLTrelloDeskId': board_creatio_id,
        }
        return self.create_object(RECEIPT_OBJECT_NAME, dict_data)
    
    def create_message_log_sms(
        self,
        mobie_phone,
        text,
    ):
        dict_data = {
            'Address': mobie_phone,
            'Text': text,
            'MessageChannelId': 'F7135347-9F65-4573-B409-6ADA0C47ADB6' # SMS
        }
        return self.create_object('MessageLog', data=dict_data)

    
    def post_phone_book(self, full_name, lead_id, phone_number):
        dict_data = {
            'UsrFullName': full_name,
            'UsrLeadId': lead_id,
            'UsrNumber': phone_number,
        }     
        return self.create_object(PHONE_BOOK_OBJECT_NAME, dict_data)

    def delete_receipt(self, receipt_creatio_id):
        status_code: int = self.delete_object(RECEIPT_OBJECT_NAME, receipt_creatio_id)
        return status_code

    def post_task(self, title, executor_creatio_id, receipt_creatio_id, hours, minutes, card_url):
        """ Создать экземпляр SLTrelloTask """
        dict_data = {
            'SLName': title,
            'SLExecutorId': executor_creatio_id,
            'SLHours': hours,
            'SLMinutes': minutes,
            'SLCardLink': card_url,
            'SLReceiptId': receipt_creatio_id,
        }
        return self.create_object(TASK_OBJECT_NAME, dict_data)

    def receipt_tasks_count(self, receipt_creatio_id):
        """ Количество тасков в рецепте в Creatio """
        if self.odata_version == ODATA_version.v3:
            url = (
                f"{self.odata_service_link}/{TASK_OBJECT_NAME}Collection" +
                f"?$filter={RECEIPT_OBJECT_NAME}/Id eq guid'{receipt_creatio_id}'"
            )
            response = requests.get(
                url= url,
                headers=self.headers,
                cookies= self.cookies,
            )
            array = json.loads(response.content)['d']['results']
        else:
            url = (
                f"{self.odata_service_link}/{TASK_OBJECT_NAME}" +
                f"?$filter={RECEIPT_OBJECT_NAME}/Id eq {receipt_creatio_id}"
            )
            response = requests.get(
                url= url,
                headers=self.headers,
                cookies= self.cookies,
            )
            array = json.loads(response.content)['value']
        return len(array)
    
    def get_object(self, object_name: str, field:str, value: str, order_by: str, order_asc: bool = True):
        """
            Object collection using filter
            doesnt support Id columns
        """
        if self.odata_version == ODATA_version.v3:
            if order_asc:
                asc = 'asc'
            else:
                asc = 'desc'
             
            url = self.odata_service_link + f"/{object_name}Collection?$filter={field} eq '{value}'&$orderby= {order_by} {asc}"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)['d']['results']
        else:
            url = self.odata_service_link + f"/{object_name}?$filter={field} eq '{value}'"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)['value']
        return result

    def get_contact_by_id(self, contact_id):
        if contact_id == None: return None
        if self.odata_version == ODATA_version.v3:
            # url = self.odata_service_link + f"/ContactCollection(guid'{contact_id}')?$select=UsrTotalLoansCount, MobilePhone, UsrOpenedLoansCount, Name, Id"
            url = self.odata_service_link + f"/ContactCollection(guid'{contact_id}')"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)['d']
        elif self.odata_version == ODATA_version.v4core or self.odata_version == ODATA_version.v4:
            url = self.odata_service_link + f"/Contact({contact_id})"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)
        else: result = None

        return result

    def get_creatio_contact_id(self, creatio_channel_id, number):
        if self.odata_version == ODATA_version.v3:
            url = self.odata_service_link + f"/ContactCommunicationCollection?$filter=CommunicationType/Id eq guid'{creatio_channel_id}' and Number eq '{number}'"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)['d']
            try:
                result = result[0]['ContactId']
            except:
                result = None
        elif self.odata_version == ODATA_version.v4core or self.odata_version == ODATA_version.v4:
            url = self.odata_service_link + f"/ContactCommunication?$filter=CommunicationType/Id eq {creatio_channel_id} and Number eq '{number}'"
            response = requests.get(
                url=url,
                headers=self.headers,
                cookies= self.cookies,
            )
            result = json.loads(response.content)
            try:
                result = result[0]['ContactId']
            except:
                result = None
        else: result = None

        return result

    