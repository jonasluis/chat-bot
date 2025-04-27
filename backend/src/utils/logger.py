import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    logger = logging.getLogger('FURIAChatbot')
    logger.setLevel(logging.INFO)

    # Criar diretório de logs se não existir
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configurar handler de arquivo
    file_handler = RotatingFileHandler(
        'logs/chatbot.log',
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(file_handler)

    return logger