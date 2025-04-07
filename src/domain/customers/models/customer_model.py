from interfaces.addressed_entity import AddressedEntity

class Customers(AddressedEntity):
    def __init__(self,
        customer_id: str, company_name: str, contact_name: str,
        contact_title: str, phone: str, fax: str):
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
        self.__customer_id = customer_id

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
        self.__fax = fax #TODO Ajustar os constraints