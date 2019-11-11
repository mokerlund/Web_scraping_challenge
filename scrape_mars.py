from bs4 import BeautifulSoup
import requests
from splinter import Browser

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

# Find Latest News Article
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)

for i in range(1):
    # Find title
    title = soup.find('div', class_="content_title")
    news_title = title.a.text
    
    # Find body
    p = soup.find_all('div', class_='rollover_description_inner')
    news_p = p[0].text
    
    print(f"Title: {news_title}")
    print(f"P: {news_p}")
# Scrape Images From NASA

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True) 

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)

image = soup.find('article', class_='carousel_item')
# print(type(image))
link_tag = image.a
# print(link_tag)
img_link = link_tag['data-fancybox-href']

ref_link = (f"https://www.jpl.nasa.gov{img_link}")
browser.visit(ref_link)

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

url = "https://twitter.com/marswxreport?lang=en"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)

first_tweet = soup.find('p', class_='tweet-text')
mars_weather = first_tweet.text

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

url = "https://space-facts.com/mars/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)

table_info = soup.find('tbody')
print(table_info.prettify())
table_string = str(table_info)

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)

results = soup.find_all('div', class_='item')
first_result = results[0]
print(first_result)

hemispheres = []
titles = []
links = []

# GO through and click on each of the links to get the actual pic url
for result in results:
    title = result.h3.text
    titles.append(title)


for i in range(0,4):
    browser.find_by_css('img.thumb')[i].click()
    sample_button = browser.find_by_text('Sample')
    img_url = sample_button['href']
    links.append(img_url)
    browser.visit(url)
    
print({"news_title" : news_title, "news_p": news_p, "ref_link": ref_link, "mars_weather": mars_weather, "table_info": table_info, "links": links, "titles": titles})