def scrape():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Find Latest News Article
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    browser.visit(url)

    for i in range(1):
        try:
            # Find title
            title = soup.find('div', class_="content_title")
            news_title = title.a.text
            
            # Find body
            p = soup.find_all('div', class_='rollover_description_inner')
            news_p = p[0].text
            
            print(f"Title: {news_title}")
            print(f"P: {news_p}")
        except AttributeError as e:
            print(e)
    
    # Scrape Images From NASA

    