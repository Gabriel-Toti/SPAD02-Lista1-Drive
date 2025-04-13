import datetime
from interfaces.database_table import DatabaseTable
from interfaces.addressed_entity import AddressedEntity

class Employee(AddressedEntity, DatabaseTable):
    def __init__(self,
        employee_id: int, last_name: str, first_name: str,
        title: str, title_of_courtesy: str, birth_date: datetime,
        hire_date: datetime, address: str=None, city: str=None, region: str=None,
        postal_code: str=None, country: str=None, home_phone: str=None, extension: str=None,
        reports_to: int=None, notes: str=None):

        super().__init__(address, city, region, postal_code, country)
        
        self._employee_id = employee_id
        self._last_name = last_name
        self._first_name = first_name
        self._title = title
        self._title_of_courtesy = title_of_courtesy
        self._birth_date = birth_date
        self._hire_date = hire_date
        self._home_phone = home_phone
        self._extension = extension
        self._reports_to = reports_to
        self._notes = notes
    
    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def title(self):
        return self.__title
    
    @property
    def title_of_courtesy(self):
        return self.__title_of_courtesy
    
    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def hire_date(self):
        return self.__hire_date
    
    @property
    def home_phone(self):
        return self.__home_phone
    
    @property
    def extension(self):
        return self.__extension
    
    @property
    def reports_to(self):
        return self.__reports_to
    
    @property
    def notes(self):
        return self.__notes
    
    @employee_id.setter
    def _employee_id(self, employee_id: int):
        self.__employee_id = employee_id

    @last_name.setter
    def _last_name(self, last_name: str):
        if(len(last_name) > 10):
            raise ValueError("Limite de caracteres excedido para last_name. max(10).")
        self.__last_name = last_name
    
    @first_name.setter
    def _first_name(self, first_name: str):
        if(len(first_name) > 10):
            raise ValueError("Limite de caracteres excedido para first_name. max(10).")
        self.__first_name = first_name
    
    @title.setter
    def _title(self, title: str):
        if(len(title) > 25):
            raise ValueError("Limite de caracteres excedido para title. max(25).")
        self.__title = title
    
    @title_of_courtesy.setter
    def _title_of_courtesy(self, title_of_courtesy: str):
        if(len(title_of_courtesy) > 5):
            raise ValueError("Limite de caracteres excedido para title_of_courtesy. max(5).")
        self.__title_of_courtesy = title_of_courtesy
    
    @birth_date.setter
    def _birth_date(self, birth_date: datetime):
        self.__birth_date = birth_date
    
    @hire_date.setter
    def _hire_date(self, hire_date: datetime):
        self.__hire_date = hire_date
    
    @home_phone.setter
    def _home_phone(self, home_phone: str):
        if(home_phone is not None and len(home_phone) > 14):
            raise ValueError("Limite de caracteres excedido para home_phone. max(14).")
        self.__home_phone = home_phone
    
    @extension.setter
    def _extension(self, extension: str):
        if(extension is not None and len(extension) > 4):
            raise ValueError("Limite de caracteres excedido para extension. max(4).")
        self.__extension = extension
    
    @reports_to.setter
    def _reports_to(self, reports_to: int):
        self.__reports_to = reports_to
    
    @notes.setter
    def _notes(self, notes: str):
        self.__notes = notes