# API Escola

Este é o repositório para o projeto de API de uma Escola feito em Django REST Framework.  
Para saber mais informações, acesse o [Trello do Projeto](https://trello.com/b/WPxbvI0c/django-rest-framework-escola-curso-01).

**⚠️ Este projeto foi desenvolvido como parte de um curso na Alura e tem finalidade exclusiva de aprendizado.**
Pretendo ampliar meus conhecimentos criando projetos pessoais cada vez mais desafiadores, com foco em soluções reais e impacto de verdade.

## 🚀 Começando

### 📦 Configuração do Ambiente Virtual (venv)

Para garantir um ambiente de desenvolvimento limpo e isolado, siga os passos:

  1. Navegue até o diretório raiz do projeto:
  
  2. Crie um novo ambiente virtual dentro do diretório do projeto:
     ``` bash
       python -m venv venv
     ```
  3. Ative o ambiente virtual. No Windows, execute:
     ``` bash
       venv/Scripts/activate
     ```
     No macOS/Linux, execute:
     ``` bash
       source venv/bin/activate
     ```
  4. Agora você está no ambiente virtual, onde pode instalar dependências necessárias para o funcionamento do projeto.

### 📥 Instalando Dependências
Você pode instalar as dependências necessárias para o projeto. Certifique-se de que o ambiente virtual está ativado antes de prosseguir. Execute o seguinte comando:
  ``` bash
     pip install -r requirements.txt
  ```
Este comando instalará todas as dependências listadas no arquivo requirements.txt.
### 🛠️ Migração do Banco de Dados
Antes de iniciar a aplicação, é necessário aplicar as migrações ao banco de dados. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
Isso aplicará todas as migrações pendentes ao banco de dados.

### ▶️ Executando a Aplicação
Após configurar o ambiente virtual, instalar as dependências e aplicar as migrações, você pode iniciar o servidor de desenvolvimento Django. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:
```bash
  python manage.py runserver
```
Isso iniciará o servidor de desenvolvimento em http://localhost:8000/. Você pode acessar este URL em seu navegador para interagir com a API.
