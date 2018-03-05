'''
    Find cheap airfares
    1. retrieving fare data with web scraping techniques
    2. parse the DOM to extract pricing data
    3. sending real-time alters using IFTTT
'''
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.by import by

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 




def check_flights():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")

    driver = webdriver.Chrome(chrome_options=options)
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
    
    url ="https://www.google.com/flights/explore/#explore;f=JFK,EWR,LGA;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=10;lx=14;d=2018-03-12"
    driver.get(url)
    driver.save_screenshot('flight_explorer.png')
    # wait = WebDriverWait(driver, 20)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.LH3SCIC-v-c')))

    # s = BeautifulSoup(driver.page_source, "lxml")
    # best_price_tags = s.findAll('div', 'LH3SCIC-w-e')
    
    # check if scrape worked  - alert ifit fails and shutdown
    # if len(best_price_tags) < 4:
    #     print('Failed to load page data')
        
if __name__ == '__main__':
    check_flights()