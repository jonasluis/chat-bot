# Chatbot da FURIA 🐺

Um chatbot interativo que representa a FURIA Esports, desenvolvido com Google Generative AI (Gemini). O bot fornece informações sobre times, jogadores, próximos jogos e interage com os fãs no estilo característico da FURIA.

## 🎮 Funcionalidades

- Interação natural com os fãs da FURIA usando emojis e hashtags
- Informações atualizadas sobre times e jogadores
- Calendário de torneios e resultados recentes
- Respostas personalizadas com o estilo FURIA
- Sistema de logging para monitoramento
- Tratamento de erros robusto

## 🛠️ Tecnologias

- Python 3.x
- Google Generative AI (Gemini)
- python-dotenv para gerenciamento de variáveis de ambiente
- Sistema de logging com RotatingFileHandler

## 📁 Estrutura do Projeto

```plaintext
chatbot/
├── src/
│   ├── config/
│   │   └── settings.py    # Configurações da API e mensagens
│   ├── core/
│   │   └── chatbot.py     # Classe principal do chatbot
│   ├── data/
│   │   └── context.py     # Contexto da FURIA e instruções
│   └── utils/
│       └── logger.py      # Sistema de logging
├── .env                   # Variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo git
├── main.py               # Ponto de entrada da aplicação
└── requirements.txt      # Dependências do projeto
```

### Instalação

1. **Clone o repositório**
    
    ```bash
    git clone git@github.com:jonasluis/chat-bot.git
    cd chat-bot
    
    ```
    
2. **Configure o ambiente Python**
    
    ```bash
    cd backend
    python -m venv venv
    
    # Windows
    .\\venv\\Scripts\\activate
    
    # Linux/macOS
    source venv/bin/activate
    
    ```
    
3. **Instale as dependências Python**
    
    ```bash
    # Instale as bibliotecas
    pip install google-generativeai
    pip install python-dotenv
    
    ```
    
4. **Configure as variáveis de ambiente**
Crie um arquivo `.env` com:
    
    ```
    GEMINI_API_KEY="[API_KEY]"
   
    
    ``` 

## 💻 Executando o Projeto

```bash
python main.py
```

5. Interaja com o chatbot digitando suas mensagens
6. Digite 'sair' para encerrar a conversa

## Logs

Os logs são armazenados no diretório `logs/` com timestamp para facilitar o rastreamento de erros e monitoramento do sistema.

## Contribuição

Sinta-se à vontade para contribuir com melhorias! 🎮

#GoFURIA #SomosFURIA 🐺