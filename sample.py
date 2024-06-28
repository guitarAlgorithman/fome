import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.df.cl'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Find the title of the webpage
    title = soup.title.string
    print('Title of the page:', title)
    
    # Example: Find all article titles
    articles = soup.find_all('h2')  # Change the tag and class as needed
    for article in articles:
        print('Article title:', article.get_text())
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)