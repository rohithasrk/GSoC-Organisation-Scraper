import requests
from bs4 import BeautifulSoup


def scrape(url):
    response = requests.get(
        url, proxies=proxies) if has_proxy else requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})
    file = open('orgs.txt', 'w')
    for org in orgs:
        org_name = org.find('h4').text
        print org_name
        org_name= org_name.encode('utf-8')
        file.write(org_name+'\n')
    file.close()
