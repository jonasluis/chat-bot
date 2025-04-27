import google.generativeai as genai
from src.config.settings import API_KEY, MODEL_NAME, WELCOME_MESSAGE, GOODBYE_MESSAGE, ERROR_MESSAGE
from src.data.context import FURIA_CONTEXT, SYSTEM_INSTRUCTIONS
from src.utils.logger import setup_logger

class FURIAChatbot:
    def __init__(self):
        self.logger = setup_logger()
        self._setup_api()
        self._initialize_chat()

    def _setup_api(self):
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel(
            MODEL_NAME,
            system_instruction=SYSTEM_INSTRUCTIONS
        )

    def _initialize_chat(self):
        self.chat = self.model.start_chat(history=[])
        print(WELCOME_MESSAGE)

    def send_message(self, message):
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            self.logger.error(f"Erro ao processar mensagem: {str(e)}")
            return ERROR_MESSAGE

    def run(self):
        while True:
            user_input = input("Você: ")
            if user_input.lower() == "sair":
                print(GOODBYE_MESSAGE)
                break
            
            response = self.send_message(user_input)
            print("FURIA:", response)