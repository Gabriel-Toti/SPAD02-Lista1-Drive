# Conexão com a base de dados
from psycopg import connect
from psycopg import OperationalError
from dotenv import load_dotenv
from os import getenv
from utils.logger import logger
from utils.error_handler import ErrorHandler

load_dotenv()

northwind = None

try:
    northwind = connect(
        host=getenv("DATABASE_HOST", "localhost"),
        dbname="northwind",
        user=getenv("DATABASE_USER", "postgres"),
        password=getenv("DATABASE_PASSWORD", "postgres")
    );
    logger.log("Conexão com a base de dados realizada com sucesso!")
except OperationalError as error:
    errorHanler = ErrorHandler()
    errorHanler.showError(errorHanler.catchError(error))