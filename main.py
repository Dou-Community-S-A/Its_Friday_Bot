# Code by: @Lostdou (Facundo Bottaro)
# Code by: @matiasdante (Matias Dante)

# date: 2024-05-01

import tweepy
import schedule
import time

# Autenticacion a twitter.
bearer_token = "Your-bearer-token"
consumer_key = "Your-consumer-key"
consumer_secret = "Your-consumer-secret"
access_token = "Your-access-token"
access_token_secret = "Your-access-token-secret"

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

# Función para comprobar si es viernes o no, y twitearlo
def horario_tweet():
    hoy=time.strftime("%A")
    if hoy=="Friday":
        tweet = client.create_tweet(
            text="Hoy es viernes"
        )
    else:
        tweet = client.create_tweet(
            text="Hoy no es viernes"
        )

schedule.every().day.at("00:00").do(horario_tweet) # Todos los dias a las 00:00 llama a la funcion horario_tweet

while True:
    schedule.run_pending() # Ejecuta las tareas pendientes
    time.sleep(1)

