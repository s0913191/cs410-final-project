import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import uuid
import json
import os
import datetime
import time

def file_existance_check(target_id: str):
    folder_path = fr"C:\temp\equipment"
    existing_file_ids = {entry.name.split("_")[0] for entry in os.scandir(folder_path) if entry.is_file()}
    return target_id in existing_file_ids

def strong_tag_text_ripper(soup: BeautifulSoup, pattern: str):
    strong_tags = soup.find_all('strong')
    for strong_tag in strong_tags:
        if strong_tag.text == pattern and strong_tag.next_sibling:
            text = strong_tag.next_sibling.strip().split(":",1)[-1].strip()
            return text
        
def table_spec_ripper(soup: BeautifulSoup):
    h4_tags = soup.find_all('h4')
    spec_dict = {}
    # Spec tables
    for h4 in h4_tags:
        if h4.next_sibling:
            table_dict = {}
            table_name = h4.get_text(strip=True)
            table = h4.find_next_sibling("table", class_="category-specs")
            rows = table.find_all('tr')            
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    table_dict[key] = value
            spec_dict[table_name] = table_dict
    return spec_dict

def scrape_one_page(url: str):
    source_url = url.replace('\r', '').replace('\n', '')
    source_url_id = url.split("/")[-1].replace('\r', '').replace('\n', '')
    source_url_model = url.split("/")[-2].replace('\r', '').replace('\n', '')
    source_url_make = url.split("/")[-3].replace('\r', '').replace('\n', '')
    source_url_category = url.split("/")[-4].replace('\r', '').replace('\n', '')
    source_date_scraped = str(datetime.datetime.now())

    if file_existance_check(source_url_id):
        print(f"Passing file: {source_url_id}")
        return
    result_dict = {}
    retries = 0
    max_retries = 5
    retry_interval = 10
    while retries < max_retries:
        try:
            res = requests.get(source_url)
            break
        except requests.ConnectionError as e:
            retries += 1
            print(f"Connection error occurred: {e}. Retrying {retries}/{max_retries}")
            retry_interval = retry_interval * retries
            time.sleep(retry_interval)
        except Exception as e:
            raise e
    soup = BeautifulSoup(res.text, "html.parser")
    
    equipment_category = strong_tag_text_ripper(soup, "Category")
    equipment_make = strong_tag_text_ripper(soup, "Manufacturer")
    equipment_model = strong_tag_text_ripper(soup, "Model")
    equipment_spec = table_spec_ripper(soup)

    for var_name, var_value in locals().items():
        if var_name.startswith(("source_","equipment_")):
            result_dict[var_name] = var_value
    
    output_dir = fr"C:\temp\equipment"
    output_file_name = fr"{source_url_id}_{source_url_category}_{source_url_make}_{source_url_model}.json"
    output_path = fr"{output_dir}/{output_file_name}"
    
    with open(output_path, 'w') as f:
        json.dump(result_dict, f, indent=4)
    
def scrape_bulk_category_make(url: str):
    # URL is for category/make
    # url = 'https://www.constructionequipmentguide.com/charts/backhoe-loaders/cukurova'
    url_prefix = 'https://www.constructionequipmentguide.com/charts'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    rows = soup.find_all('tr', attrs={'data-url': True})
    urls = [url_prefix+row['data-url'] for row in rows]

    for url in urls:
        scrape_one_page(url)

def scrape_bulk_category(url: str):
    # URL is for category
    # url = 'https://www.constructionequipmentguide.com/charts/backhoe-loaders'
    url_prefix = 'https://www.constructionequipmentguide.com'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    div_element = soup.find('div', class_='manufacturers-grid columns-three-responsive')
    links = div_element.find_all('a')
    urls = [url_prefix+link['href'] for link in links]
    
    for url in urls:
        print(url.split("/")[-1])
        scrape_bulk_category_make(url)

def scrape_bulk_top(url: str):
    # URL is for top
    # url = 'https://www.constructionequipmentguide.com/equipment-specs-and-charts'
    urls = []
    url_prefix = 'https://www.constructionequipmentguide.com'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    div_elements = soup.find_all('div', class_='grid-list')
    for div_element in div_elements:
        links = div_element.find_all('a')
        for link in links:
            urls.append(url_prefix+link['href'])
    #print(urls)
    
    for url in urls:
        print(url+'\n')
        scrape_bulk_category(url)


if __name__ == "__main__":
    scrape_bulk_top('https://www.constructionequipmentguide.com/equipment-specs-and-charts')