import urllib.request as urllib2
import json
import pprint

ip = input("Enter Ip --> : ")
url = "http://ip-api.com/json/"+ip+"?fields=country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting,query"

response = urllib2.urlopen(url)
data = response.read()
values = json.loads(data)

pprint.pprint(values)