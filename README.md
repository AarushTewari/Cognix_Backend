This is the repository which stores the backend code for my work @Cognix Technologies. The work involves creating the backend architecture of a Yoga Assistant App.

# Locally setting up the project

## Create a file called keyconfig.py in the same folder as your settings.py file and add the following code 

```python

from os import path

DATABASE_ENGINE = "django.db.backends.mysql"
DATABASE_USER = "YOUR MYSQL USERNAME"
DATABASE_PASSWORD = "YOUR MYSQL PASSWORD"
DATABASE_PORT = "YOUR DATABASE PORT"
DATABASE_NAME = "YOUR DATABASE NAME"

CREDENTIALS_JSON = path.join(path.dirname(path.realpath(__file__)), "config", "file.json")

```
## Now in the same folder create a folder called config and inside it create a file name file.json and add the following code

```json

{
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
  "universe_domain": ""
}

```

Run the follwoing commands

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver

```

Now the project can be accessed at http://127.0.0.1:8000/.
