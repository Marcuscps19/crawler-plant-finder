from parsel import Selector
import requests
import time
from w3lib.html import remove_tags


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


def get_scientific_name(selector):
    return selector.css('#custom_type_fields ul li em::text').get()


def trim_array(array):
    return [s.replace(" ", "") for s in array]


def remove_commas(array):
    return [s.replace(",", " ") for s in array]


def strip_array(array):
    return [s.strip(" ") for s in array]


def remove_empty_items(array):
    [array.remove(item) for item in array if item == '']
    return array


def format_array(array):
    trimmed_array = trim_array(array)
    commas_removed = remove_commas(trimmed_array)
    stripped_array = strip_array(commas_removed)
    empty_items_removed = remove_empty_items(stripped_array)
    if(empty_items_removed):
        return empty_items_removed[0].split(' ')
    return []


def get_popular_names(selector):
    lis_tags = selector.css('#custom_type_fields ul li')
    if(len(lis_tags) == 9):
        popular_names = selector.css(
            '#custom_type_fields ul li:nth-child(2)::text').getall()
    else:
        popular_names = selector.css(
            '#custom_type_fields ul li:nth-child(3)::text').getall()
    return format_array(popular_names)


def get_by_href_text(selector, text):
    str = selector.css(
        f'#custom_type_fields ul li a[href*="{text}"]::text').getall()
    return str if str else []


def get_description(selector):
    parent_html = selector.css('.post-entry').get()
    # Source remove_tags:
    # https://stackoverflow.com/questions/54140416/scrapy-removing-html-tags-in-a-list-output
    parent_html_without_tags = remove_tags(
        parent_html, which_ones=('em', 'strong', 'a'))
    selector_without_tags = Selector(
        text=parent_html_without_tags, type="html")
    all_p_tags = selector_without_tags.css('p').getall()
    new_strings = []
    for p_tag in all_p_tags:
        new_string = p_tag.replace('<p>', '').replace('</p>', '\n')
        new_strings.append(new_string)
    return ''.join(new_strings)


def get_src_by_id(selector, id):
    return selector.css(f'#{id}::attr(src)').get()


def get_photographer_info(selector):
    name = selector.css('.wp-caption-text a::text').get()
    personal_page = selector.css('.wp-caption-text a::attr(href)').get()
    if(personal_page):
        if(personal_page[0] == '/'):
            personal_page = 'https://www.jardineiro.net' + personal_page
            return {'name': name, 'personal_page': personal_page}
    return None


def get_author(selector):
    name = selector.css('span[itemprop="name"]::text').get()
    personal_page = selector.css('.author a::attr(href)').get()
    return {'name': name, 'personal_page': personal_page}


def get_source(selector):
    return selector.css('link[rel="canonical"]::attr(href)').get()


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
        print(plants_infos)
        print('\n')
    return plants_infos


def plants_infos():
    html_content = fetch(
        'https://www.jardineiro.net/plantas-de-a-a-z-por-nome-popular')
    plants_links = scrape_plants(html_content)
    plants_infos = get_plants_infos(plants_links)
    return plants_infos


if __name__ == '__main__':
    plants_infos()
