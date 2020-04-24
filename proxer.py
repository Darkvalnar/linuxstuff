#!/usr/bin python

__author__ = 'Rawlings'
__contact__ = 'sh0t@hashbang.sh'

import requests
from bs4 import BeautifulSoup

counter = 0
# the proxy site(s) we are scraping
proxyDomain = "https://free-proxy-list.net/"

# let the user decide which name and format for the list is being used
filename = input("Target name for proxylist (without format): ")
fileformat = input("Target format for proxy list: ")

# we make a get request to the website
r = requests.get(proxyDomain)

# now we store the content of the website in a variable by using BeautifulSoup and the python html parser
soup = BeautifulSoup(r.content, 'html.parser')

# now we let BeautifulSoup scan the parsed content, we are using the table tag since the target is a table (duh) and look for its specified ID within the HTML code
# we are also using a dictionary for this
table = soup.find("table", {"id" : "proxylisttable"})

# now we run a for loop to parse the entirety of the table (by using find_all), we will then filter all table rows and table coloumns
for row in table.find_all("tr"):
    coloumns = row.find_all("td")
    
# we need to use a try statement to mitigate possible blank lines
# we will now start fetching the IP and port of the listed servers, we store those contents in the content variable by grabbing index 0 for IP and index 1 for PORT
# should there be a fail, we'll keep on scraping
    try:
       
        content = "%s:%s" %(coloumns[0].get_text(),coloumns[1].get_text())
        counter +=1
# now we're cooking with gas and create a file to store our proxies in, of course with a linebreak, we're not savages
        f = open(filename + fileformat, "a")
        f.write (content + "\n")
        f.close()
    except:
        pass

       
print ("Storing " + str(counter) + " IPs in " + filename + fileformat)
print ("Welcome to flavortown baby")
