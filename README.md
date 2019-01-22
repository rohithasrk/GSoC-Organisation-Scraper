# GSoC Organisation Scraper

Makes life easier by scraping instead of searching for each and every organisation by name. Also shows number of times that an organisation has appeared in GSoC.
Used [Requests](http://docs.python-requests.org/en/master/) library of python and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Use Python-*2.7*

### Requirements :
+ BeautifulSoup
+ Requests

### Instructions :

```bash
# Clone this repository
git clone https://github.com/rohithasrk/GSoC-Organisation-Scraper.git

# Go into the repository
cd GSoC-Organisation-Scraper

# Install dependencies
[sudo] pip2 install -r requirements.txt

# Run the app without giving technology as a command line argument 
python2 scrape.py

# Enter the technology of preference when prompted.
# Example: python

# Run the app by giving technology as a command line argument 
python2 scrape.py javascript

#To store the output to a text file use pipe
python2 scrape.py ruby > ruby_orgs
```

### Screenshots :

When browsed for javascript and ruby, some of the results are as shown below.

![Python orgs 1](img/pyorgs.png)

![Python orgs 2](img/pyorgs2.png)

### TODOs :
+ Make the code run faster.
+ Remove multiple results.

### Contributing :
+ Fork the repo.
+ Create a new branch named `<your_feature>`
+ Commit changes and make a PR.
+ PRs are welcome.

This program uses PyTerm-Colors : https://github.com/vinamarora8/PyTerm-Colors.git
