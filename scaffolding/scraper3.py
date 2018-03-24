# From DataCamp course "Importing Data in Python (Part 2)"
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: 
r = requests.get(url)

# Extracts the response as html: 
html_doc = r.text

# create a BeautifulSoup object from the HTML: 
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): 
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
