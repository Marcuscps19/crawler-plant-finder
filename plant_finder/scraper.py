from parsel import Selector
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


def scrape_plants(html_content):
    selector = Selector(text=html_content)
    plants_links = selector.css('.pt-cv-ifield a::attr(href)').getall()
    if(plants_links):
        return plants_links
    return []


def get_plants_infos(links):
    plants_infos = []
    for link in links:
        page_info = fetch(link)
        selector = Selector(text=page_info)
        plants_infos.append(get_info_by_plant(selector))
    return plants_infos


def plants_infos():
    html_content = fetch(
        'https://www.jardineiro.net/plantas-de-a-a-z-por-nome-popular')
    plants_links = scrape_plants(html_content)
    plants_infos = get_plants_infos(plants_links)

