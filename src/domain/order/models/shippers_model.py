from interfaces.database_table import DatabaseTable
class Shipper(DatabaseTable):
    def __init__(self, shipper_id: int, company_name: str, phone: str):
        self._shipper_id = shipper_id
        self._company_name = company_name
        self._phone = phone
    
    @property
    def shipper_id(self):
        return self.__shipper_id
    
    @property
    def company_name(self):
        return self.__company_name
    
    @property
    def phone(self):
        return self.__phone
    
    @shipper_id.setter
    def _shipper_id(self, shipper_id: int):
        self.__shipper_id = shipper_id
    
    @company_name.setter
    def _company_name(self, company_name: int):
        self.__company_name = company_name

    @phone.setter
    def _phone(self, phone: int):
        self.__phone = phone