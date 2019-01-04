#!/usr/bin/env python
import os
import signal
import sys
import warnings

import requests
from bs4 import BeautifulSoup

from resources.pyterm_colors import pyterm_colors

url = "https://summerofcode.withgoogle.com/archive/2018/organizations/"
default = "https://summerofcode.withgoogle.com"
dir_path = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)),
    'resources')

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
                    color.yellow + str(number + 1) + '\n' + color.default
                count += 1

    if count == 0:
        print color.red + "Enter a valid technology name." + color.default


def no_of_times(org_name):
    count = 0
    try:
        for year in range(2009, 2018):
            fil = open(os.path.join(dir_path, '{}.txt'.format(str(year))),
                       'r').read().split('\n')
            if org_name in fil:
                count += 1
    except Exception as e:
        print(str(e))

    return count


if __name__ == "__main__":
    scrape()
