from functools import wraps
from sys import stderr

from loguru import logger

logger.remove()  # Remove a configuração padrão do logger

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO",
)

logger.add(
    "meu_arquivo_de_logs_critical.log",  # Arquivo específico para logs críticos
    format="{time} {level} {message} {file}",
    level="INFO",
)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Executando a função {func.__name__} com args {args} e  kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função {func.__name__} retornou {result}")
            return result
        except Exception as e:
            logger.critical(f"Erro na função {func.__name__}: {e}")
            raise

    return wrapper
