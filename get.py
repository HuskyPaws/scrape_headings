# Import the BeautifulSoup and requests modules
from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL of the page you want to scrape
url = 'https://topdogtips.com/best-dog-booties/'
data = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

# Find all the heading tags on the page
headings = soup.find_all(['h1', 'h2', 'h3'])

# Print the text of each heading
for heading in headings:
  print(heading.get_text())
