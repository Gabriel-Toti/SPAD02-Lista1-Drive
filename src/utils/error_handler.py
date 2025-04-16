from .errors.out_of_stock_exception import OutOfStockException
from .errors.not_found_exception import NotFoundException
from utils.logger import logger, MessageLevel
from tkinter import messagebox
from psycopg import OperationalError

class ErrorHandler():
    def __init__(self):
        pass
    
    @staticmethod
    def catchError(error: Exception): # Gerar uma mensagem de erro

        if type(error) == ValueError:
            return logger.log(error=error, level=MessageLevel.WARNING)

        if type(error) == NotFoundException:
            return logger.log(error=error, level=MessageLevel.WARNING)

        if type(error) == OutOfStockException:
            return logger.log(error=error, level=MessageLevel.WARNING)

        if type(error) == OperationalError:
            if error.pgconn.status == 1:
                return logger.log(error=error, level=MessageLevel.FATAL)
            else: return logger.log(error=error, level=MessageLevel.ERROR)

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