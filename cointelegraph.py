import requests 
from bs4 import BeautifulSoup
import csv

url = "https://cointelegraph.com/ico-calendar"
r = requests.get(url)

soup = BeautifulSoup(r.content)

# links = soup.find_all ("a")

# for link in links :
# 	if "http" in link.get("href"):
# 	    print ("link = '%s' si link text ='%s'" %(link.get("href"), link.text))

# g_data = soup.find_all ("div", {"class": "table-companies__item j-item"});

# for item in g_data: print (item.text) 



# for item in g_data: 
# 	print (item.contents[1].find_all("div", {"class":"table-companies__item-ttl"})[0].text)
# 	print (item.contents[1].find_all("div", {"class":"table-companies__item-desc"})[0].text)
# 	print (item.contents[1].find_all("div", {"class":"table-companies__item-date"})[0].text)
# 	try: print (item.contents[1].find_all("div", {"class":"table-companies__item-days"})[0].text)
# 	except: pass



with open ('/users/cipsy/DC/telegraph.csv','w') as outfile:
	csv_writer= csv.writer (outfile)
	csv_writer.writerow (["Name", "Description", "GoLive", "Days"])
	for item in g_data:
		name= (item.contents[1].find_all("div", {"class":"table-companies__item-ttl"})[0].text)
		desc= (item.contents[1].find_all("div", {"class":"table-companies__item-desc"})[0].text)
		date= (item.contents[1].find_all("div", {"class":"table-companies__item-date"})[0].text)
		try: days= (item.contents[1].find_all("div", {"class":"table-companies__item-days"})[0].text)
		except: pass
		csv_writer.writerow ([name, desc, date, days])