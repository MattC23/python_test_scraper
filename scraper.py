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

# print tds

indexno = 0
# This creates a variable we can use as a unique key

for td in tds:
  indexno = indexno + 1
  # This ensures the variable indexno is a unique key 
  record = {"cell" : td.text, "index" : indexno}
  # This creates a dictionary variable called 'record' with two sets of data in it
  scraperwiki.sqlite.save(["index"], record)
  # This states that index is the unique key, and also says that the variable 'record' should be added to the database
  
#  print "HTML tag and text:", lxml.html.tostring(td)
#  print "HTML text:", td.text

