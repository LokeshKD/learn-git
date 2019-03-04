#!/usr/bin/python


###
## Code to get the HTML page of options URL from nseindia.
###

import httplib
#import http.client

c = httplib.HTTPSConnection("www.nseindia.com")
#c = http.client.HTTPSConnection("www.nseindia.com")
c.request("GET", "/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument=OPTIDX&symbol=NIFTY&date=27DEC2018")
response = c.getresponse()

print response.status, response.reason
#200 OK

data = response.read()

f = open("test.txt", "w+")
f.write(data)
f.close()

###
### Parsing HTML
###

import BeautifulSoup
soup = BeautifulSoup.BeautifulSoup
p_html = soup(data)

print p_html.prettify()


