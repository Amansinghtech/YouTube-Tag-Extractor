from bs4 import BeautifulSoup
# from selenium import webdriver
import json
# import time
import urllib.request as req

# options = webdriver.ChromeOptions()
# options.add_argument("--log-level=3")

# driver = webdriver.Chrome('chromedriver.exe', options=options)
# driver.get('https://www.youtube.com/watch?v=EtgSZGWb2m0&t=18s')
# content = driver.page_source
content = req.urlopen('https://www.youtube.com/watch?v=EtgSZGWb2m0&t=18s')
# time.sleep(5)
# driver.close()
def tag_extractor(content):
    soup = BeautifulSoup(content, 'html.parser')
    for script in soup.findAll('script'):
        if 'keywords' in str(script):    
            start_ind = str(script).index('keywords')
            start_ind += 10
            rest_out = str(str(script)[start_ind:])
            end_ind = rest_out.index(']')
            final = rest_out[:end_ind+1]
            final = final.replace('\\', '')
            final = final.replace(':', '')
            return (json.loads(final))

print(tag_extractor(content))