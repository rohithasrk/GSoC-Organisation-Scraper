#!/usr/bin/env python
import os
import signal
import sys
import warnings

import requests

from bs4 import BeautifulSoup
from resources.pyterm_colors import pyterm_colors

url = "https://summerofcode.withgoogle.com/archive/2017/organizations/"
default = "https://summerofcode.withgoogle.com"
prev_def_url = "https://www.google-melange.com/archive/gsoc/"
url16 = "https://summerofcode.withgoogle.com/archive/2016/organizations/"
dir_path = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)),
    'resources')

o2009 = open(os.path.join(dir_path, '2009.txt'), 'r').read().split('\n')
o2010 = open(os.path.join(dir_path, '2010.txt'), 'r').read().split('\n')
o2011 = open(os.path.join(dir_path, '2011.txt'), 'r').read().split('\n')
o2012 = open(os.path.join(dir_path, '2012.txt'), 'r').read().split('\n')
o2013 = open(os.path.join(dir_path, '2013.txt'), 'r').read().split('\n')
o2014 = open(os.path.join(dir_path, '2014.txt'), 'r').read().split('\n')
o2015 = open(os.path.join(dir_path, '2015.txt'), 'r').read().split('\n')
o2016 = open(os.path.join(dir_path, '2016.txt'), 'r').read().split('\n')
o2017 = open(os.path.join(dir_path, '2017.txt'), 'r').read().split('\n')

# For proxy support
has_proxy = False
proxies = {}
try:
    proxies = {
        'http': os.environ['http_proxy'],
        'https': os.environ['https_proxy'],
    }
    has_proxy = True
    print "Proxy detected\n"
except KeyError:
    pass

# For colored output
color = pyterm_colors.color()

# To avoid warning messages
warnings.filterwarnings("ignore")


def signal_handler(signal, frame):
    confirmation = raw_input(
        color.red +
        "Really want to exit (y/n)? " +
        color.default)
    confirmation.replace(" ", "")
    confirmation = confirmation.lower()
    if confirmation == "y" or confirmation == "yes":
        sys.exit(0)
    else:
        return


signal.signal(signal.SIGINT, signal_handler)


def scrape():
    if(len(sys.argv) == 2):
        user_pref = sys.argv[1]
    else:
        user_pref = raw_input(
            color.yellow +
            "Enter a technology of preference: " +
            color.default)
    user_pref = user_pref.lower()
    user_pref.replace(" ", "")
    count = 0

    response = requests.get(
        url, proxies=proxies) if has_proxy else requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})

    for org in orgs:
        link = org.find('a', attrs={'class': 'organization-card__link'})
        org_name = org['aria-label']
        org_link = default + link['href']
        response = requests.get(
            org_link, proxies=proxies) if has_proxy else requests.get(org_link)
        html = response.content
        soup = BeautifulSoup(html)
        tags = soup.findAll('li', attrs={
            'class': 'organization__tag organization__tag--technology'
        }
        )
        for tag in tags:
            if user_pref in tag.text:
                number = no_of_times(org_name)
                print color.default + "Name: " + color.cyan + org_name
                print color.default + "Link: " + color.blue + org_link
                print color.default + "No. of times in GSoC: " + \
                    color.yellow + str(number) + '\n' + color.default
                count += 1

    if count == 0:
        print color.red + "Enter a valid technology name." + color.default


def no_of_times_before_2016(org_name):
    count = 0
    for i in range(2009, 2016):
        year_url = prev_def_url + str(i)
        response = requests.get(
            year_url, proxies=proxies) if has_proxy else requests.get(year_url)
        html = response.content
        soup = BeautifulSoup(html)
        orgs = soup.findAll('li', attrs={
            'class': 'mdl-list__item mdl-list__item--one-line'
        }
        )
        for org in orgs:
            name = org.find('a').text
            if org_name == name:
                count += 1
                break
    return count


def orgs_of_an_year(year):
    year_url = prev_def_url + year
    response = requests.get(
        year_url,
        proxies=proxies) if has_proxy else requests.get(year_url)
    html = response.content
    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={
        'class': 'mdl-list__item mdl-list__item--one-line'
    }
    )
    for org in orgs:
        org_name = org.find('a').text
        print org_name


def scrape16():
    response = requests.get(
        url16, proxies=proxies) if has_proxy else requests.get(url16)
    html = response.content
    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})
    file = open('2016.txt', 'w')
    for org in orgs:
        orgss = org.find('h4').text
        print orgss
        orgsss = orgss.encode('utf-8')
        file.write(orgsss+'\n')
    file.close()


def no_of_times(org_name):
    count = 0
    try:
        if org_name in o2009:
            count += 1
        if org_name in o2010:
            count += 1
        if org_name in o2011:
            count += 1
        if org_name in o2012:
            count += 1
        if org_name in o2013:
            count += 1
        if org_name in o2014:
            count += 1
        if org_name in o2015:
            count += 1
        if org_name in o2016:
            count += 1
        if org_name in o2017:
            count += 1
    except Exception as e:
        print(str(e))

    return count


if __name__ == "__main__":
    scrape()
