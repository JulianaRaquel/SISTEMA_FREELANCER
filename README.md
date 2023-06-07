# Sistema de projetos para Freelancers

### Objetivo: desenvolvimento de um sistema para que freelancers possam pesquisar e selecionar projetos de acordo com a sua área de atuação e realizar o envio dos  projetos finalizados.

## Tecnologias Utilizadas:
* ### Python
* ### Django
* ### Git
* ### PostgreSQL
* ### Docker

## Funcionalidades do Projeto

### 1. Sistema de cadastro de usuário (http://127.0.0.1:8000/cadastro/)
### 2. Sistema de login de usuário (http://127.0.0.1:8000/logar/)
### 3. Página com a listagem dos projetos disponíveis e filtragem por preço mínimo, preço máximo, prazo mínimo, prazo máximo e categoria. (http://127.0.0.1:8000/encontrar_jobs/)
### 4. Modal contendo as informações do projeto com botão para que o usuário possa aceitar o projeto.
### 5. Página de perfil individual para usuário com formulário para edição de suas informações pessoais. (http://127.0.0.1:8000/perfil/)
### 6. Histórico dos projetos selecionados pelo usuário na página de perfil informando o status atual do projeto. (http://127.0.0.1:8000/perfil/)
### 7. Modal para que o usuário possa fazer o envio do projeto finalizado. 

## Instruções para instalação

### Faça o clone do projeto:
```commandline
git clone git@github.com:JulianaRaquel/SISTEMA_FREELANCER.git
```

### Crie o ambiente virtual:
```commandline
python3 -m venv venv
```

### Ative o ambiente virtual no linux:
```commandline
source venv/bin/activate
```

### Ative o ambiente virtual no windows:
```commandline
env\Scripts\Activate
```

### Instale as dependências:
```commandline
pip install -r requirements.txt
```

### Copie as variáveis de ambiente:
```commandline
cp .env.example .env
```

### Aplique as migrações:
```commandline
python3 manage.py migrate
```

### Rode o servidor:
```commandline
python3 manage.py runserver
```

