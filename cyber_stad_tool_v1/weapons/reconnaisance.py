import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

def fetch_data(url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        data = urlopen(url, context=ctx).read()
        return data
    except Exception as e:
        print(str(e))
        return None

def parse_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)

def gather_vulnerabilities(url):
    data = fetch_data(url)
    if data is not None:
        parse_data(data)
    else:
        print("Unable to fetch data.")

gather_vulnerabilities('https://myshop.cstad.shop')