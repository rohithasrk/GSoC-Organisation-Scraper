#!/usr/bin/env python
import requests
from BeautifulSoup import BeautifulSoup
import signal
import sys

url = "https://summerofcode.withgoogle.com/archive/2016/organizations/"
default = "https://summerofcode.withgoogle.com"
prev_def_url = "https://www.google-melange.com/archive/gsoc/"

def signal_handler(signal, frame):
  confirmation = raw_input("Really want to exit (y/n)? ")
  confirmation.replace(" ","")
  confirmation = confirmation.lower()
  if confirmation == "y" or confirmation == "yes":
    sys.exit(0)
  else :
    return

signal.signal(signal.SIGINT, signal_handler)

def scrape():
  user_pref = raw_input("Enter a technology of preference: ")
  user_pref = user_pref.lower()
  user_pref.replace(" ","")
  count = 0

  response = requests.get(url)
  html = response.content

  soup = BeautifulSoup(html)
  orgs = soup.findAll('li', attrs={'class':'organization-card__container'})

  for org in orgs:
    link = org.find('a', attrs={'class':'organization-card__link'})
    org_name = org['aria-label']
    org_link = default+link['href']
    response = requests.get(org_link)
    html = response.content
    soup = BeautifulSoup(html)
    tags = soup.findAll('li', attrs={'class':'organization__tag organization__tag--technology'})
    for tag in tags:
      if user_pref in tag.text:
        print "Name: "+org_name
        print "Link: "+org_link + '\n'
        count += 1

  if count == 0:
    print "Enter a valid technology name."

if __name__=="__main__":
  scrape()
  
