# cadastro-e-login

API em Python (FastAPI + SQLite) para cadastro de usuários, login com JWT e acesso a uma rota protegida.

## Rotas

| Método | Rota        | Descrição                                       |
| ------ | ----------- | ----------------------------------------------- |
| POST   | `/register` | Cadastra um usuário (`name`, `email`, `password`) |
| POST   | `/login`    | Retorna um token JWT (`email`, `password`)       |
| GET    | `/profile`  | Retorna nome e e-mail do usuário autenticado     |

## Ambiente virtual e dependências

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Executando o servidor

```bash
uvicorn main:app --reload
```

O servidor sobe em `http://127.0.0.1:8000` e o banco `users.db` é criado automaticamente.

## Testando a API

Com o servidor rodando, acesse `http://127.0.0.1:8000/docs`, a documentação interativa gerada pelo FastAPI:

1. Em **POST /register**, clique em **Try it out**, preencha nome, e-mail e senha e clique em **Execute** (retorna `201`).
2. Em **POST /login**, faça o mesmo com e-mail e senha e copie o `access_token` da resposta.
3. Acesse a rota protegida enviando o token no header `Authorization`:

```bash
curl.exe http://127.0.0.1:8000/profile -H "Authorization: Bearer <token>"
```

Sem token, ou com um token inválido ou expirado, a resposta é `401`.
