# cadastro-e-login

API em Python (FastAPI + SQLite) para cadastro de usuários, login com JWT e acesso a uma rota protegida.

## Rotas

| Método | Rota        | Descrição                                                        |
| ------ | ----------- | ---------------------------------------------------------------- |
| POST   | `/register` | Cadastra um usuário (JSON: `name`, `email`, `password`)          |
| POST   | `/token`    | Retorna um token JWT (formulário: `username` = e-mail, `password`) |
| GET    | `/users/me` | Retorna nome e e-mail do usuário autenticado                     |

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
2. Clique em **Authorize**, informe o e-mail no campo `username` e a senha no campo `password`.
3. Em **GET /users/me**, clique em **Try it out** e **Execute**: o token é enviado automaticamente.

Sem token, ou com um token inválido ou expirado, a resposta é `401`.

Também é possível testar pelo Postman: no `/token`, envie o corpo como `x-www-form-urlencoded`, e no `/users/me`, use o token na aba **Authorization** com o tipo **Bearer Token**.
