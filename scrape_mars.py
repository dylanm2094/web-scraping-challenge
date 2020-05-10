from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
import pymongo
import pandas as pd
import re


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    final_dict = {}

    #Looking for the latest new article
    url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url_news)

    html = browser.html
    soup = bs(html, "html.parser")
    soup

    final_dict["headline"] = soup.find("div", class_='list_text').find("div", class_='content_title').text
    final_dict["teaser"] = soup.find("div", class_='list_text').find("div", class_='article_teaser_body').text
    
    #Grabbing the featured image
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    feat_img = soup.find("div", class_='carousel_items').find("article", class_='carousel_item').find("a")['data-fancybox-href']
    final_dict["feat_img"] = f"https://www.jpl.nasa.gov{feat_img}"

    #Getting the weather from twitter
    url_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_twitter)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    final_dict["weather"] = soup.find("div", class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').find("span").text

    #Getting Mars facts
    url_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_facts)

    df = tables[0]
    mars_facts = df.to_html()

    final_dict["mars_facts"] = mars_facts

    #Getting Hemisphere iamages
    hemisphere_image_urls = []
    hem_dict = {}

    #syrtis_major
    url_sm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_sm)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    sm_title = soup.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    sm_img = soup.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    sm_image_url = f"https://astrogeology.usgs.gov{sm_img}"

    hem_dict["title"] = sm_title
    hem_dict["img_url"] = sm_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    #valles_marineris
    url_vm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_vm)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    vm_title = soup.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    vm_img = soup.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    vm_image_url = f"https://astrogeology.usgs.gov{vm_img}"

    hem_dict["title"] = vm_title
    hem_dict["img_url"] = vm_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    #schiaparelli
    url_sch = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_sch)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    sch_title = soup.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    sch_img = soup.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    sch_image_url = f"https://astrogeology.usgs.gov{sch_img}"

    hem_dict["title"] = sch_title
    hem_dict["img_url"] = sch_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    #cerberus
    url_cer = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_cer)

    html = browser.html
    soup = bs(html, 'html.parser')
    soup

    cer_title = soup.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    cer_img = soup.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    cer_image_url = f"https://astrogeology.usgs.gov{cer_img}"

    hem_dict["title"] = cer_title
    hem_dict["img_url"] = cer_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    final_dict["hem_img_urls"] = hemisphere_image_urls

    browser.quit()

    return final_dict