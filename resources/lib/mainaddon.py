import requests
import re
from bs4 import BeautifulSoup

url1 = "https://asic.podbean.com/feed.xml"

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://asic.podbean.com/feed.xml")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item' limit=9):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/859234/ASIC_Podcast_large_size.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
