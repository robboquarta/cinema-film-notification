import requests
from bs4 import BeautifulSoup
import boto3

def lambda_handler(event, context):
    url = "https://www.cineworldtrento.it/film-al-cinema/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    film = "Mission Impossible"

    # Cerca il film "Mission Impossible" nella lista dei film 
    links_film_titoli = soup.find_all("h3") # Cerca tra i titoli dei film siano in tag <h3>
    for link_film_titolo in links_film_titoli:
        film_titolo = link_film_titolo.get_text(strip=True)
        if film.lower() in film_titolo.lower():
            print("Notifica inviata!")
            invia_notifica()
            return True

def invia_notifica():
    sns = boto3.client('sns', region_name='us-east-2')  # Regione AWS su cui è stato deployato il servizio SNS
    topic_arn = "arn:aws:sns:us-east-2:657463212482:CinemaNotify"  # Topic ARN

    messaggio = "🎬 'Mission Impossible' è ora disponibile su Cineworld Trento!"
    sns.publish(
        TopicArn=topic_arn,
        Message=messaggio,
        Subject="Notifica Film Disponibile"
    )
