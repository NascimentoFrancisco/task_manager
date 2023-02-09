# Desafio Django: Aplicação de Tarefas

## Principais tecnologias usadas
- Python 3.8.10
- Django 4.1.4

## Instruções para usar esse projeto em sua máquina local

1º) Clone o repositŕorio com o seguinte comando:
~~~
https://github.com/NascimentoFrancisco/task_manager.git
~~~

2º) Abra oprojeto em seu editor de texto de preferência para criar e ativar o virtualenv
> Windows:

Criação
~~~
python -m venv venv
~~~
Ativação
~~~
venv\Scripts\activate
~~~

> Linux:

Criação
~~~
python3 -m venv venv
~~~
Ativação
~~~
. venv/bin/activate
~~~

3º) Instale as dependências
~~~
pip install -r requirements.txt
~~~

4º) Faça as migrations e o migrate

~~~
python manage.py makemigrations
~~~
~~~
python manage.py migrate
~~~

5º) Configure os dados do arquivo `.env` da seguinte forma:

**OBS:** Antes de inserir os dados de seu e-mail nessa aplicação faça as configurações em sua conta google.

* Acesse o gmail e vá na opção `Gerencie sua Conta do Google`.
* Depois vá no menu lateral e acesse a opção `Segurança`.
* Logo procure a opção `Fazendo login no Google` nesse tópico vá em `senhas de aplicaivos`.
* Crie um aplicativo de senhas, copie a senha e a atribua ao campo `EMAIL_PASSWORD` do arquivo `.env`.

~~~
DEBUG=False ou True
SECRET_KEY='Sua SECRET_KEY'
EMAIL_HOST_USER='Seu e-mail'
EMAIL_PASSWORD='Senha de seu e-mail'
~~~

6º) Inicie o servidor e acesse o seguinte link

~~~
python manage.py runserver
~~~
~~~
http://127.0.0.1:8000/
~~~