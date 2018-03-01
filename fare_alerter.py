from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import by

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from sklearn.cluster imort DBSCAN
from sklearn.preprocessing import StandardScaler

from schedule
from time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 


def check_flights():
    url ="https://www.google.co.in/flights/explore/#explore;f=JFK,EWR,LGA;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=8;lx=12;d=2016-11-29"
    driver = webdriver.PhantomJS()
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true'])
    driver.implicitly_wait(20)
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.LH3SCIC-v-c')))

    s = BeautifulSoup(driver.page_source, "lxml")
    best_price_tags = s.findAll('div', 'LH3SCIC-w-e')
    
    # check if scrape worked  - alert ifit fails and shutdown
    if len(best_price_tags) < 4:
        print('Failed to load page data')