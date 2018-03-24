# From DataCamp course "Importing Data in Python (Part 2)"
import requests
from bs4 import BeautifulSoup

# Specify url: 
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: 
r = requests.get(url)

# Extracts the response as html: 
html_doc = r.text

# Create a BeautifulSoup object from the HTML: 
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: 
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)
