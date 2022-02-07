import requests
import time


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)
        if(response.status_code == 200):
            return response.text
        return None
    except requests.Timeout:
        return None

def plants_infos():
    html_content = fetch(
        'https://www.jardineiro.net/plantas-de-a-a-z-por-nome-popular')
