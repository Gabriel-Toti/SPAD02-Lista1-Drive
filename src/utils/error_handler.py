from utils.logger import logger, MessageLevel
from tkinter import messagebox
from psycopg import OperationalError

class ErrorHandler():
    def __init__(self):
        pass
    
    @staticmethod
    def catchError(error: Exception): # Gerar uma mensagem de erro
        #TODO: Adicionar os tipos de erros da aplicação para fazer a verificação
        if type(error) == OperationalError:
            if error.pgconn.status == 1:
                return logger.log(error=error, level=MessageLevel.FATAL)

        return logger.log(error=error, level=MessageLevel.ERROR)

    @staticmethod
    def showError(error: dict[str, str]): # Exibir o erro em um modal de mensagem
        if error["level"] == MessageLevel.ERROR.value:
            messagebox.showerror(error["level"], error["message"])
        elif error["level"] == MessageLevel.WARNING.value:
            messagebox.showwarning(error["level"], error["message"])
        elif error["level"] == MessageLevel.FATAL.value:
            messagebox.showerror(error["level"], error["message"])
            logger.create_log_file()
            exit(1)