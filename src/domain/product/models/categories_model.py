class Category():
    def __init__(self, category_id: int, category_name: str, description: str):
        self._category_id = category_id
        self._category_name = category_name
        self._description = description
    #? Então aqui eu não uso um array de objetos por exemplo?

    @property
    def category_id(self):
        return self.__category_id
    
    @property
    def category_name(self):
        return self.__category_name
    
    @property
    def description(self):
        return self.__description
    
    @category_id.setter
    def _category_id(self, category_id: int):
        self.__category_id = category_id
    
    @category_name.setter
    def _category_name(self, category_name: str):
        self.__category_name = category_name

    @description.setter
    def _description(self, description: int): #TODO: Validações vêm aqui
        self.__description = description