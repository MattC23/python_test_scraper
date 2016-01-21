import scraperwiki
import lxml.html

html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
print html
