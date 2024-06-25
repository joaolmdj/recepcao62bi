# Recepção 62º BI

Este é um projeto desenvolvido em Django e Python para registrar a entrada e saída dos visitantes na organização militar do Exército Brasileiro. Este sistema foi criado para ser utilizado pelo 62º Batalhão de Infantaria, visando otimizar e automatizar o processo de recepção de visitantes.

![system](https://github.com/joaolmdj/recepcao62bi/assets/61760730/29448e1e-6549-4ec3-be93-1e3cf2dcb5b3)

## Funcionalidades

- Registro de visitantes na entrada.
- Registro de qual seção dentro da OM o visitante foi.
- Registro de visitantes na saída.
- Relatórios de visitas diárias.
- Análise de dados
- Controle de acesso para administradores e operadores.
- Interface amigável e fácil de usar.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework Web**: Django
- **Banco de Dados**: Postgresql (pode ser configurado para usar outros bancos de dados)
- **Frontend**: HTML, CSS, JavaScript
- **Conteinerização**: Docker

## Requisitos

- Python 3.8 ou superior
- Docker Desktop

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/joaolmdj/recepcao62bi.git
   cd recepcao62bi
   ```

2. Rode o build do docker-compose:
   ```bash
   docker-compose up --build
   ```

3. Crie um superusuário para acessar o admin do Django:
   ```bash
   python manage.py createsuperuser
   ```
   Ou durate a execução do docker-compose
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   
4. Acesse o sistema em seu navegador:
   ```
   http://127.0.0.1:8000
   localhost:8000
   ```

## Configuração

### Configurações do Banco de Dados

O projeto está configurado para rodar o Postgresql dentro da imagem Docker, você pode alterar o .settings e rodar apenas com SQLite.

### Variáveis de Ambiente

Você pode usar um arquivo `.env` seguindo como exemplo o `.env-exemple` para configurar variáveis de ambiente, como chaves secretas e configurações de banco de dados. Exemplo de um arquivo `.env`:

```env
SECRET_KEY='sua-chave-secreta'
DEBUG=True
DATABASE_URL='postgres://usuario:senha@localhost:5432/nome_do_banco'
```

---

**Desenvolvido para o 62º Batalhão de Infantaria do Exército Brasileiro**
**@joaolmdj**
