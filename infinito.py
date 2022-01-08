from datetime import datetime, timezone
from pytz import timezone
import time
import pyrebase

config = {
  "apiKey": "AIzaSyCNn0mGaCUkII5spLfDsZ0L6MVYtks1U-c",
  "authDomain": "projeto-horario.firebaseapp.com",
  "databaseURL": "https://projeto-horario-default-rtdb.firebaseio.com",
  "projectId": "projeto-horario",
  "storageBucket": "projeto-horario.appspot.com",
  "messagingSenderId": "821513709417",
  "appId": "1:821513709417:web:f7ebb137d32ab8afb7bff8",
  "measurementId": "G-5ECQ74S9T2"
}

firebase = pyrebase.initialize_app(config)
horario = firebase.database()

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d')
data_e_hora_sao_paulo_em_texto2 = data_e_hora_sao_paulo.strftime('%m')
data_e_hora_sao_paulo_em_texto3 = data_e_hora_sao_paulo.strftime('%Y')
data_e_hora_sao_paulo_em_texto4 = data_e_hora_sao_paulo.strftime('%H')
data_e_hora_sao_paulo_em_texto5 = data_e_hora_sao_paulo.strftime('%M')
data_e_hora_sao_paulo_em_texto0 = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
while True:
        print(data_e_hora_sao_paulo_em_texto)
        print(data_e_hora_sao_paulo_em_texto2)
        print(data_e_hora_sao_paulo_em_texto3)
        print(data_e_hora_sao_paulo_em_texto4)
        print(data_e_hora_sao_paulo_em_texto5)
        print(data_e_hora_sao_paulo_em_texto0)
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d')
        data_e_hora_sao_paulo_em_texto2 = data_e_hora_sao_paulo.strftime('%m')
        data_e_hora_sao_paulo_em_texto3 = data_e_hora_sao_paulo.strftime('%Y')
        data_e_hora_sao_paulo_em_texto4 = data_e_hora_sao_paulo.strftime('%H')
        data_e_hora_sao_paulo_em_texto5 = data_e_hora_sao_paulo.strftime('%M')
        data_e_hora_sao_paulo_em_texto0 = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
        horario.child('info').update({"dia": data_e_hora_sao_paulo_em_texto})
        horario.child('info').update({"mês": data_e_hora_sao_paulo_em_texto2})
        horario.child('info').update({"ano": data_e_hora_sao_paulo_em_texto3})
        horario.child('info').update({"horas": data_e_hora_sao_paulo_em_texto4})
        horario.child('info').update({"minutos": data_e_hora_sao_paulo_em_texto5})
        time.sleep(60)