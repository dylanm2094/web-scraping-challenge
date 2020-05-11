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
    final_dict = {}

    #Looking for the latest new article
    browser = init_browser()
    url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url_news)

    html_news = browser.html
    soup_news = bs(html_news, "html.parser")
    soup_news

    final_dict["headline"] = soup_news.find("div", class_='list_text').find("div", class_='content_title').text
    final_dict["teaser"] = soup_news.find("div", class_='list_text').find("div", class_='article_teaser_body').text

    browser.quit()
    
    #Grabbing the featured image
    browser = init_browser()
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)

    html_img = browser.html
    soup_img = bs(html_img, 'html.parser')
    soup_img

    feat_img = soup_img.find("div", class_='carousel_items').find("article", class_='carousel_item').find("a")['data-fancybox-href']
    final_dict["feat_img"] = f"https://www.jpl.nasa.gov{feat_img}"

    browser.quit()

   

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
    browser = init_browser()
    url_sm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_sm)

    html_sm = browser.html
    soup_sm = bs(html_sm, 'html.parser')
    soup_sm

    sm_title = soup_sm.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    sm_img = soup_sm.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    sm_image_url = f"https://astrogeology.usgs.gov{sm_img}"

    hem_dict["title"] = sm_title
    hem_dict["img_url"] = sm_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    browser.quit()

    #valles_marineris
    browser = init_browser()
    url_vm = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_vm)

    html_vm = browser.html
    soup_vm = bs(html_vm, 'html.parser')
    soup_vm

    vm_title = soup_vm.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    vm_img = soup_vm.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    vm_image_url = f"https://astrogeology.usgs.gov{vm_img}"

    hem_dict["title"] = vm_title
    hem_dict["img_url"] = vm_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    browser.quit()

    #schiaparelli
    browser = init_browser()
    url_sch = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_sch)

    html_sch = browser.html
    soup_sch = bs(html_sch, 'html.parser')
    soup_sch

    sch_title = soup_sch.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    sch_img = soup_sch.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    sch_image_url = f"https://astrogeology.usgs.gov{sch_img}"

    hem_dict["title"] = sch_title
    hem_dict["img_url"] = sch_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    browser.quit()

    #cerberus
    browser = init_browser()
    url_cer = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_cer)

    html_cer = browser.html
    soup_cer = bs(html_cer, 'html.parser')
    soup_cer

    cer_title = soup_cer.find("div", class_='content').find("section", class_='block metadata').find('h2').text
    cer_img = soup_cer.find("div", class_='wide-image-wrapper').find("img", class_='wide-image')['src']
    cer_image_url = f"https://astrogeology.usgs.gov{cer_img}"

    hem_dict["title"] = cer_title
    hem_dict["img_url"] = cer_image_url

    hemisphere_image_urls.append(dict(hem_dict))

    final_dict["hem_img_urls"] = hemisphere_image_urls

    browser.quit()

    return final_dict