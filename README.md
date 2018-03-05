## Reference
    - Python Machine Learning Projects -Udemy
    - https://my.oschina.net/leejun2005/blog/407043

## Setup
```
$ virtualenv --system-site-packages -p python3 venv3

$ . venv3/bin/activate

(venv3)$ pip3 install -r requirements.txt

...
(venv3)$ deactivate

brew install phantomjs
```


## About Selenium, chromedriver and PhantomJS
Install selenium
```
pip install selenium
```
Using PhantomJS
```
driver = webdriver.PhantomJS()
```    
causes warning
```
Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
```
So PhantomJS should be replaced with chrome driver. To fix error
```
selenium.common.exceptions.WebDriverException: Message: ‘chromedriver’ executable needs to be in PATH.
```
We should download chromedriver at https://sites.google.com/a/chromium.org/chromedriver/downloads, when put it into 
virtual environment/bin