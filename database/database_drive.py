# Conexão com a base de dados
from psycopg import connect
from psycopg import OperationalError
from dotenv import load_dotenv
from os import getenv
from src.utils.logger import logger
from src.utils.error_handler import ErrorHandler
from psycopg import Connection


load_dotenv()

__connection_options = {
    "host":getenv("DATABASE_HOST", "localhost"),
    "dbname":"northwind",
    "user":getenv("DATABASE_USER", "postgres"),
    "password":getenv("DATABASE_PASSWORD", "postgres")
}

def database() -> Connection:
    logger.log(f"Tentando conexão em {__connection_options['host']} com {__connection_options['dbname']}...")
    try:

        northwind = connect(
            host=__connection_options["host"],
            dbname=__connection_options["dbname"],
            user=__connection_options["user"],
            password=__connection_options["password"]
        );
        logger.log("Conexão com a base de dados realizada com sucesso!")
        return northwind
    except OperationalError as error:
        errorHanler = ErrorHandler()
        errorHanler.showError(errorHanler.catchError(error))
        return None

# def transaction(*ops: callable, params: dict[int, list[any]]):
#     with database() as connection:
#         with connection.cursor() as session:
#             for func, param in params.items():
#                 ops[func](*param, session)