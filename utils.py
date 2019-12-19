import os

import requests
from bs4 import BeautifulSoup

# For proxy support
has_proxy = False
proxies = {}
try:
    proxies = {
        'http': os.environ['http_proxy'],
        'https': os.environ['https_proxy'],
    }
    has_proxy = True
    print ("Proxy detected\n")
except KeyError:
    pass


def scrape(url):
    response = requests.get(
        url, proxies=proxies) if has_proxy else requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})
    file = open('orgs.txt', 'w')
    for org in orgs:
        org_name = org.find('h4').text
        print (org_name)
        org_name = org_name.encode('utf-8')
        file.write(org_name+'\n')
    file.close()
