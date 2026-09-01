# Chatbot---Telegram
# Mentor.IA

Mentor.IA é um chatbot para Telegram desenvolvido em Python com o objetivo de oferecer orientação prática sobre comunicação profissional e comportamento organizacional.

A proposta surgiu a partir da identificação de uma necessidade de treinamento em empresas, especialmente em áreas relacionadas à comunicação, vendas e contato com o público.

## Funcionalidades

* Conversação com inteligência artificial pelo Telegram.
* Histórico das últimas 10 mensagens de cada usuário.
* Respostas direcionadas para situações do ambiente profissional.
* Orientações curtas, práticas e objetivas.
* Integração com a API da OpenRouter.
* Indicador de que o bot está processando a mensagem.

## Tecnologias utilizadas

* Python
* Telegram Bot API
* pyTelegramBotAPI
* OpenRouter API
* DeepSeek
* Requests
* python-dotenv

## Estrutura do projeto

```text
Mentor.IA/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/Mentor.IA.git
cd Mentor.IA
```

### 2. Crie um ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto.

Use o `.env.example` como referência:

```env
TOKEN_TELEGRAM=seu_token_do_telegram
TOKEN_OPENROUTER=sua_chave_da_openrouter
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 5. Execute o bot

```bash
python main.py
```

Se tudo estiver configurado corretamente, o terminal exibirá:

```text
bot iniciado!
```

## Como funciona

Quando um usuário envia uma mensagem, o bot registra a mensagem no histórico daquela conversa e envia o histórico recente para o modelo de inteligência artificial.

A IA recebe um prompt específico para atuar como uma mentora voltada à comunicação profissional e ao comportamento organizacional.

O histórico é limitado às 10 mensagens mais recentes para manter o contexto da conversa sem enviar uma quantidade excessiva de dados para a API.

## Variáveis de ambiente

O projeto utiliza duas variáveis de ambiente:

| Variável           | Descrição                                        |
| ------------------ | ------------------------------------------------ |
| `TOKEN_TELEGRAM`   | Token utilizado para acessar o bot do Telegram   |
| `TOKEN_OPENROUTER` | Chave utilizada para acessar a API da OpenRouter |

Nunca publique essas chaves diretamente no código ou no GitHub.

## Limitações atuais

O histórico das conversas é armazenado apenas na memória enquanto o programa está em execução. Caso o bot seja reiniciado, os históricos são perdidos.

O projeto também utiliza long polling, portanto o bot precisa manter o programa em execução para continuar recebendo mensagens.

## Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Persistência do histórico em banco de dados.
* Sistema de autenticação de usuários.
* Comandos adicionais no Telegram.
* Interface administrativa.
* Métricas de utilização.
* Deploy em um servidor.
* Melhor tratamento de erros da API.
* Personalização das respostas de acordo com diferentes situações profissionais.

## Licença

Este projeto está disponível para fins educacionais e de portfólio.

