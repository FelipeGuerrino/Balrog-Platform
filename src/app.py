import pyrebase

firebaseConfig={'apiKey': "AIzaSyA5oftsNguj-ppC1PaKvEO4Yiw1oMylSMY",
    'authDomain': "balrogbot-10a80.firebaseapp.com",
    'databaseURL': "https://www.balrogbot-10a80.firebase.io.com",
    'projectId': "balrogbot-10a80",
    'storageBucket': "balrogbot-10a80.appspot.com",
    'messagingSenderId': "87745930958",
    'appId': "1:87745930958:web:aad167518ed129623d529f",
    'measurementId': "G-KMK6GTSM1P"}

app=pyrebase.initialize_app(firebaseConfig)

auth=app.auth()

email=input("insira seu email: \n")
senha=input("insira sua senha: \n")

if(auth.sign_in_with_email_and_password(email, senha)):
    print("logado com sucesso!")