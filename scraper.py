import scraperwiki
# This imports the scraperwiki library

html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
# Scraperwiki.scrape function will grab all of the html on one page
# print html
# This will display the html that's been grabbed

import lxml.html
# This imports the lxml library

root = lxml.html.fromstring(html)
# lxml.html.fromstring function will convert a string into an object/variable that lxml can work with. 
# If you don't do this then you won't be able to use lxml's cssselect function

tds = root.cssselect('td')
# cssselect function will grab particular elements from a page, e.g. td tags, tr tags, li tags

print tds

for td in tds:
  print lxml.html.tostring(td)
  print td.text

