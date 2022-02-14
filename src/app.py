import pyrebase, os
from dotenv import load_dotenv

load_dotenv()

firebaseConfig={'apiKey': os.getenv('KEY'),
    'authDomain': os.getenv('AUTH'),
    'databaseURL': os.getenv('DB'),
    'projectId': os.getenv('PROJECT'),
    'storageBucket': os.getenv('BUCKET'),
    'messagingSenderId': os.getenv('SENDER'),
    'appId': os.getenv('APP'),
    'measurementId': os.getenv('MEASUREMENT')}

app=pyrebase.initialize_app(firebaseConfig)

auth=app.auth()

email=input("insira seu email: \n")
senha=input("insira sua senha: \n")

if(auth.sign_in_with_email_and_password(email, senha)):
    print("logado com sucesso!")