import urllib.request as urllib2, json, pprint

ip = input("Enter Ip --> : ")
url = "http://ip-api.com/json/"+ip+"?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

response = urllib2.urlopen(url)
data = response.read()
values = json.loads(data)

print("Not Always Accurate!")
pprint.pprint(values)
print("Not Always Accurate!")
