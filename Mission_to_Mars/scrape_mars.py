from splinter import Browser
from bs4 import BeautifulSoup 
import time
import requests
import os
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    import os
    if os.name=="nt":
        executable_path = {'executable_path': './chromedriver.exe'}
    else:
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()   

# NASA Mars News

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1.5)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    try:
        article = soup.find('div', class_='list_text')
        # article = soup.select_one('ul.item_list li.slide')
        news_title = article.find('div', class_='content_title').get_text()
        news_p = soup.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        news_title = None
        news_p = None
 
    # browser.quit()
   
# Mars Image
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(1.5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find('a',class_='button')['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov/'+image
 
# Mars Weather

    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)
    time.sleep(1.5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   
    mars_weather = soup.find_all('span')
    # weather = None
    for tweet in mars_weather:
        if'InSight sol' in tweet.text:
            mars_weather = tweet.text
            mars_weather = mars_weather.replace('InSight','')
            print(f"Mars Weather:{mars_weather}")
            break

 # Mars Facts
    url_facts ='https://space-facts.com/mars/'
    browser.visit(url_facts)
    time.sleep(1.5)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    facts_tables = pd.read_html(url_facts)
    facts_df = facts_tables[0]
    facts_df.columns=["description","value"]
    facts_df.set_index("description",inplace=True)
    del facts_df.index.name
    html_table = (facts_df.to_html()).replace('\n', '')

 # Mars Hemispheres 

    url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemispheres)
    time.sleep(1.5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('img', class_='thumb')
    hemisphere_image_urls = []
    for item in items:
        hemisphere_image_urls.append({
        'title': item['alt'].replace('thumbnail', ''),
        'img_url': 'https://astrogeology.usgs.gov/' + item['src']
    })
    browser.quit()

    mars_info= {
       "news_title": news_title,
       "news_p": news_p,
       "featured_image_url": featured_image_url,
       "mars_weather": mars_weather,
       "html_table": html_table,
       "hemisphere_image_urls": hemisphere_image_urls
    }

    return mars_info  

