# Web-Scraping-Challenge

This challenge is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# Final Result
![mission_to_mars](img/Mars1.png)

![mission_to_mars](img/Mars2.png)

![mission_to_mars](img/Mars3.png)

# Scraping URLs

1. [NASA Mars News Site](https://mars.nasa.gov/news/)
2. [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
3. [Mars Weather](https://twitter.com/marswxreport?lang=en)
4. [Mars Facts](https://space-facts.com/mars/)
5. [USGS Astrogeology Site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

# Steps

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
* Store the return value in Mongo as a Python dictionary.
* Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
