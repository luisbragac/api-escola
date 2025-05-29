# API Escola

API RESTful para gerenciamento de uma escola, desenvolvida com Django REST Framework.

> Projeto criado como parte do curso [Django REST Framework: construindo APIs RESTful do Zero](https://cursos.alura.com.br/course/django-rest-framework-construindo-apis-restful-zero) da Alura. Embora tenha fins educacionais, este repositório serve como ponto de partida para projetos mais robustos e aplicações reais.

 [Trello do Projeto](https://trello.com/b/WPxbvI0c/django-rest-framework-escola-curso-01)

## Tecnologias
- Python
- Django 
- Django REST Framework 

## Funcionalidades

- CRUD completo de Alunos, Cursos e Matrículas
- Visualização de matrículas por aluno
- Visualização de matrículas por curso
- Autenticação básica (via BasicAuth)

## Melhorias Futuras
- Validações
- Paginação
- Filtros
- Versionamento

## Tutorial
Abaixo uma lista de comandos para clonar e configurar este projeto na sua máquina local:

### Configuração do Ambiente Virtual (venv)

Crie um ambiente virtual:

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

### Instalando Dependências
Agora você pode instalar as dependências necessárias para o projeto. Lembre de que o ambiente virtual deve estar ativado antes de prosseguir. Execute o seguinte comando:
  ``` bash
     pip install -r requirements.txt
  ```
Este comando instalará todas as dependências listadas no arquivo requirements.txt.
### Migração do Banco de Dados
Antes de iniciar a aplicação, é necessário aplicar as migrações ao banco de dados. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
Isso aplicará todas as migrações pendentes ao banco de dados.

### Executando a Aplicação
Após configurar o ambiente virtual, instalar as dependências e aplicar as migrações, você pode iniciar o servidor de desenvolvimento Django. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:
```bash
  python manage.py runserver
```
Isso iniciará o servidor de desenvolvimento em http://localhost:8000/. Você pode acessar este URL em seu navegador para interagir com a API.

## ⚠️ Aviso
Este projeto tem fins exclusivamente educacionais e não deve ser usado em produção sem ajustes de segurança e escalabilidade. Foi criado como exercício prático no curso da Alura e serve como base para aplicações reais.
