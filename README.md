## Reference
    - Python Machine Learning Projects - Udemy
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
ChromeDriver is the little bit of glue that allows Selenium to send commands to Chrome and automate it. 
If you are on a Mac, to install it like 
```
brew install chromedriver
```
Or download chromedriver at https://sites.google.com/a/chromium.org/chromedriver/downloads, when put it into 
virtual environment/bin


## Trouble shooting
```
Explore Flight has not been optimized for your browser. For best results, please try Chrome, Firefox 3.5+, Internet Explorer 8+, Safari 4+. 
```