from bs4 import BeautifulSoup
import json
import requests as req
import urllib.parse as par

keyword = input("Enter a Keyword:")
while keyword == '' or keyword == ' ':
    print("Invalid input detected")
    keyword = input("Enter a Keyword:")

def walker(keyword):    
    search = {'search_query':keyword}
    url =  'https://www.youtube.com/results?{}'.format(par.urlencode(search))
    print("Url Generated: "+url)
    content = req.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')    
    a_tags = soup.findAll("a", attrs={"class": "yt-uix-sessionlink spf-link", "aria-hidden":"true"})
    for tag in a_tags:
        if "/watch" in tag['href']:
            yield tag['href']

def tag_extractor(url):
    content = req.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')
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

final = []

for link in walker(keyword):
    url = 'https://www.youtube.com' + link
    out = tag_extractor(url)
    if out is not None:
        print(out)
        final += out

with open('sample.txt', 'w') as file:
    json.dump(final, file, indent=2)