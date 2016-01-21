import scraperwiki
import lxml.html

html = scraperwiki.scrape("uk.soccerway.com/teams/netherlands/fortuna-sittard/")
print html
