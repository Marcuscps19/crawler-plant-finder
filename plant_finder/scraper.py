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


def get_info_by_plant(selector):
    return {
        "scientific_name": get_scientific_name(selector),
        "popular_names": get_popular_names(selector),
        "family": get_by_href_text(selector, "familia"),
        "categories": get_by_href_text(selector, "classe"),
        "climates": get_by_href_text(selector, "clima"),
        "origin": get_by_href_text(selector, "origem"),
        "height": get_by_href_text(selector, "altura"),
        "luminosity": get_by_href_text(selector, "luminosidade"),
        "life_cycle": get_by_href_text(selector, "ciclo"),
        "description": get_description(selector),
        "image": get_src_by_id(selector, "post_image"),
        "photographer": get_photographer_info(selector),
        "author": get_author(selector),
        "source":  get_source(selector)
    }


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

