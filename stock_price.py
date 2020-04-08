import re
import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
Ticker = 'TSTL'
url = 'http://www.lse.co.uk/SharePrice.asp?shareprice=' + Ticker
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

for line in tags:
    if re.search('"sp_sharePrice sp_' + Ticker + '_MID" data-field="sharePrice"',str(line)):
        print(Ticker, re.findall('([0-9]+.[0-9]+)', str(line))[0])