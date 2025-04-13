from interfaces.addressed_entity import AddressedEntity
from interfaces.database_table import DatabaseTable

class Customer(AddressedEntity, DatabaseTable):
    def __init__(self,
        customer_id: str, company_name: str, contact_name: str,
        contact_title: str, address: str=None, city: str=None, region: str=None,
        postal_code: str=None, country: str=None, phone: str=None, fax: str=None):

        super().__init__(address, city, region, postal_code, country)

        self._customer_id = customer_id
        self._company_name = company_name
        self._contact_name = contact_name
        self._contact_title = contact_title
        self._phone = phone
        self._fax = fax
    
    @property
    def customer_id(self):
        return self.__customer_id
    
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
    
    @customer_id.setter
    def _customer_id(self, customer_id: str):
        
        if(len(customer_id) > 5):
            raise ValueError("Limite de caracteres excedido para customer_id. max(5).")
        
        self.__customer_id = customer_id

    @company_name.setter
    def _company_name(self, company_name: str):

        if(len(company_name) > 50):
            raise ValueError("Limite de caracteres excedido para company_name. max(50).")

        self.__company_name = company_name
    
    @contact_name.setter
    def _contact_name(self, contact_name: str):
        if(len(contact_name) > 30):
            raise ValueError("Limite de caracteres excedido para contact_name. max(30).")
        
        self.__contact_name = contact_name

    @contact_title.setter
    def _contact_title(self, contact_title: str):
        if(len(contact_title) > 30):
            raise ValueError("Limite de caracteres excedido para contact_title. max(30).")
        
        self.__contact_title = contact_title
    
    @phone.setter
    def _phone(self, phone: str):
        if(phone is not None and len(phone) > 17):
            raise ValueError("Limite de caracteres excedido para phone. max(17).")
        
        self.__phone = phone

    @fax.setter
    def _fax(self, fax: str):
        if(fax is not None and len(fax) > 17):
            raise ValueError("Limite de caracteres excedido para fax. max(17).")
        
        self.__fax = fax