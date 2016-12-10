#!/usr/bin/env python
import requests
from BeautifulSoup import BeautifulSoup
import signal
import sys
import os

url = "https://summerofcode.withgoogle.com/archive/2016/organizations/"
default = "https://summerofcode.withgoogle.com"
prev_def_url = "https://www.google-melange.com/archive/gsoc/"
dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

o2009 = open(os.path.join(dir_path, '2009.txt'), 'r').read().split('\n')
o2010 = open(os.path.join(dir_path, '2010.txt'), 'r').read().split('\n')
o2011 = open(os.path.join(dir_path, '2011.txt'), 'r').read().split('\n')
o2012 = open(os.path.join(dir_path, '2012.txt'), 'r').read().split('\n')
o2013 = open(os.path.join(dir_path, '2013.txt'), 'r').read().split('\n')
o2014 = open(os.path.join(dir_path, '2014.txt'), 'r').read().split('\n')
o2015 = open(os.path.join(dir_path, '2015.txt'), 'r').read().split('\n')


def signal_handler(signal, frame):
    confirmation = raw_input("Really want to exit (y/n)? ")
    confirmation.replace(" ", "")
    confirmation = confirmation.lower()
    if confirmation == "y" or confirmation == "yes":
        sys.exit(0)
    else:
        return


signal.signal(signal.SIGINT, signal_handler)


def scrape():
    user_pref = raw_input("Enter a technology of preference: ")
    user_pref = user_pref.lower()
    user_pref.replace(" ", "")
    count = 0

    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={'class': 'organization-card__container'})

    for org in orgs:
        link = org.find('a', attrs={'class': 'organization-card__link'})
        org_name = org['aria-label']
        org_link = default + link['href']
        response = requests.get(org_link)
        html = response.content
        soup = BeautifulSoup(html)
        tags = soup.findAll('li', attrs={
                'class': 'organization__tag organization__tag--technology'
                }
            )
        for tag in tags:
            if user_pref in tag.text:
                number = no_of_times(org_name)
                print "Name: " + org_name
                print "Link: " + org_link
                print "No. of times in GSoC: " + str(number + 1) + '\n'
                count += 1

    if count == 0:
        print "Enter a valid technology name."


def no_of_times_before_2016(org_name):
    count = 0
    for i in range(2009, 2016):
        year_url = prev_def_url + str(i)
        response = requests.get(year_url)
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
    response = requests.get(year_url)
    html = response.content
    soup = BeautifulSoup(html)
    orgs = soup.findAll('li', attrs={
            'class': 'mdl-list__item mdl-list__item--one-line'
            }
        )
    for org in orgs:
        org_name = org.find('a').text
        print org_name


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
    except:
        pass

    return count


if __name__ == "__main__":
    scrape()
