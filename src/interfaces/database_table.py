from datetime import date
class DatabaseTable():
    def __init__(self):
        pass

    def __str__(self):
        string = ""
        for nome, valor in self.__dict__.items():
            string += f"{nome.replace('_' + self.__class__.__name__ + '__', '')}: {valor};\n"
        return string
    
    def  attributes(self):
        attributes = []

        for attribute in self.__dict__.values():
            if(attribute == None):
                continue
            attributes.append(str(attribute) if type(attribute) != int else attribute)

        return tuple(attributes)