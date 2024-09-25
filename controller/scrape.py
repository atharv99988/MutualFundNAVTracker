import requests
import re
from bs4 import BeautifulSoup

def getNAVAndGrowth(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    span = soup.find_all(name='span', string='NAV', limit=1)
    if span:
        siblings = span[0].find_next_siblings(name='span')
        navPattern = r'₹\s\d+(?:\.\d+)?'
        growthPattern = r'\d+(?:\.\d+)?+%'
        nav = ''
        growth = ''
        for sibling in siblings:
            sibling_text = sibling.get_text(strip=True)
            foundNav = re.findall(navPattern, sibling_text)
            foundGrowth = re.findall(growthPattern, sibling_text)
            if len(foundNav) > 0:     # need to do because we alse get matching empty string
                nav = foundNav[0]
            if len(foundGrowth) > 0:   # need to do because we alse get matching empty string
                growth = foundGrowth[0]
        return [nav, growth]
    else:
        return []



