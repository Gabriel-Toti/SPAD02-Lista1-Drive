from interfaces.addressed_entity import AddressedEntity
from interfaces.database_table import DatabaseTable

class Supplier(AddressedEntity, DatabaseTable):
    def __init__(self,
        supplier_id: int, company_name: str, contact_name: str,
        contact_title: str, phone: str, fax: str, home_page: str):

        self._supplier_id = supplier_id
        self._company_name = company_name
        self._contact_name = contact_name
        self._contact_title = contact_title
        self._phone = phone
        self._fax = fax
        self._home_page = home_page
    
    @property
    def supplier_id(self):
        return self.__supplier_id
    
    @property
    def company_name(self):
        return self.__company_name
    
    @property
    def contact_name(self):
        return self.__contact_name
    
    @property
    def contact_title(self):
        return self.__contact_title
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def fax(self):
        return self.__fax

    @property
    def home_page(self):
        return self.__home_page
    
    @supplier_id.setter
    def _supplier_id(self, supplier_id: int):
        self.__supplier_id = supplier_id
    
    @company_name.setter
    def _company_name(self, company_name: str):
        self.__company_name = company_name

    @contact_name.setter
    def _contact_name(self, contact_name: str):
        self.__contact_name = contact_name
    
    @contact_title.setter
    def _contact_title(self, contact_title: str):
        self.__contact_title = contact_title
    
    @phone.setter
    def _phone(self, phone: str):
        self.__phone = phone

    @fax.setter
    def _fax(self, fax: str):
        self.__fax = fax
    
    @home_page.setter
    def _home_page(self, home_page: str):
        self.__home_page = home_page