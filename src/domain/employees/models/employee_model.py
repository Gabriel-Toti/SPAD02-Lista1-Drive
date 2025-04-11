import datetime
from interfaces.database_table import DatabaseTable
from interfaces.addressed_entity import AddressedEntity

class Employee(AddressedEntity, DatabaseTable):
    def __init__(self,
        employee_id: int, last_name: str, first_name: str,
        title: str, title_of_courtesy: str, birth_date: datetime,
        hire_date: datetime, home_phone: str, extension: str,
        reports_to: int, notes: str):
        
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
        self.__last_name = last_name
    
    @first_name.setter
    def _first_name(self, first_name: str):
        self.__first_name = first_name
    
    @title.setter
    def _title(self, title: str):
        self.__title = title
    
    @title_of_courtesy.setter
    def _title_of_courtesy(self, title_of_courtesy: str):
        self.__title_of_courtesy = title_of_courtesy
    
    @birth_date.setter
    def _birth_date(self, birth_date: datetime):
        self.__birth_date = birth_date
    
    @hire_date.setter
    def _hire_date(self, hire_date: datetime):
        self.__hire_date = hire_date
    
    @home_phone.setter
    def _home_phone(self, home_phone: str):
        self.__home_phone = home_phone
    
    @extension.setter
    def _extension(self, extension: str):
        self.__extension = extension
    
    @reports_to.setter
    def _reports_to(self, reports_to: int):
        self.__reports_to = reports_to
    
    @notes.setter
    def _notes(self, notes: str):
        self.__notes = notes