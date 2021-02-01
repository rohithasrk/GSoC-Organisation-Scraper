#!/usr/bin/env python

import requests
import datetime
from bs4 import BeautifulSoup

current_date = datetime.datetime.now()
current_year = current_date.year

query_year = raw_input("Enter a year from 2016 to " + str(current_year) + "\n")

# typecase query_year from string to integer
query_year = int(query_year)

#Validate input year
if(query_year < current_year and query_year >= 2016):
    print("\nWait a sec...\n")
else:
    print("Oops! Invalid year selected. Try Again")
    exit()
    
url = "https://summerofcode.withgoogle.com/archive/" + str(query_year) + "/organizations/"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html.parser")

orgs = soup.find_all("h4", class_="organization-card__name font-black-54")

print("Here you go...")
print("=============================================================\n")

#Print the names or the organisations
for org in orgs:
    name = org.text
    print(name)
