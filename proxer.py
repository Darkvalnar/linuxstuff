#!/usr/bin python

__author__ = 'Rawlings'
__contact__ = 'sh0t@hashbang.sh'

# grabbing dependencies
import sys
import requests
from bs4 import BeautifulSoup

counter = 0
liner =  ("-----------------------------------------------------------------")
liner2 = ("#################################################################")

print (r"""\
        ██████╗ ██████╗  ██████╗ ██╗  ██╗██████╗ ██████╗ 
        ██╔══██╗██╔══██╗██╔═████╗╚██╗██╔╝╚════██╗██╔══██╗
        ██████╔╝██████╔╝██║██╔██║ ╚███╔╝  █████╔╝██████╔╝
        ██╔═══╝ ██╔══██╗████╔╝██║ ██╔██╗  ╚═══██╗██╔══██╗
        ██║     ██║  ██║╚██████╔╝██╔╝ ██╗██████╔╝██║  ██║
        ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝
""")
print (liner2)

# let the user decide which name and format for the list is being used
print ("Pr0x3r, made by Rawlings.")
print (liner)
input("Press any key to continue")
print (liner2)

filename = input("Target name for proxylist (without format): ")
fileformat = input("Target format for proxy list: ")
filepath = filename + fileformat


# the setup function where we declare the proxy website and which site we check it against
# right now the simple version of canihazip is pretty good for that, however it is not neccessary
def setup():
    print ("Got IP checker and Proxywebsite")
    # the website we use to check if our proxies work, using simple version of canihazip for simplicity
    url = "https://www.canihazip.com/s"

    # the proxy site(s) we are scraping
    proxyDomain = "https://free-proxy-list.net/"

    return url, proxyDomain;

# the actual proxy fetcher starts operating here
def fetch():
    
    print ("Loading fetcher..")
    url, proxyDomain = setup()
    counter = 0
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
            f = open(filepath, "a")
            f.write ("\n" + content)
            f.close()
        except:
            pass

       
    print ("Fetched " + str(counter) + " proxies")
    print (liner2)
    choice = input("Would you like to scan all proxies now? (y/n) ")
    
    if choice == "y":
    
        return content, counter;
    if choice == "n":
    
        fetchquest = input("Fetch proxies again? (y/n) ")
        if fetchquest == "y":
            fetch()
        
        if fetchquest == "n":
            print("Exiting pr0x3r..")
            exit()

# function setup to check ALL fetched proxies    
def checker():
    print ("Loading checker..")
    url, proxyDomain = setup()
    content, counter = fetch()
    print ("Welcome to flavortown baby")
    print (liner2)
    print ("Checking " + str(counter) + " proxies." + "\n" + "This may take a while, you should grab a coffee!")
    print (liner2)
    counter = 0
    # Hey, let's make a list!
    IPs = []

    # And while we're at it, let's check those proxies, yea?

    # First, we need to open the file and read it line per line to fetch the proxy IPs and ports
    with open(filepath) as fp:
        line = fp.readline()
        cntr = 1
        # Now we start the while function to grab ALL the proxies, until there are no more lines left
        while line:
       
       
            # This is where we format the file content to make it usable, we store it in the ip variable
            ip = ("{}".format(line.strip()))
       
       
            # We'll set up our proxies with the IPs 
            proxies = { 
            "http": "http://" + ip,
            "https": "http://" + ip,
            }
       
            # You're almost in the money now, this is the important part
            try:

            # We will now attempt to send a GET request to our specified URL via the proxy with a moderate timeout
                print (" Connecting to service via " + ip + "...")
                proxycheck = requests.get(url, timeout=10, proxies=proxies)
        
                # Since the target URL only displays the proxy IP and nothing else, we will parse this with BeautifulSoup
                proxyconfirm = BeautifulSoup(proxycheck.content, "html.parser")
        
                # Now you're in the money cuz the proxy works!
                # As a bonus, to confirm it actually does work, we print the contents of the target URL
                print (" " + str(proxyconfirm) + " works!")
                print(liner)
        
                # Time to push this proxy onto the good-boy list and count one up
                IPs.append(str(ip))
                counter +=1
                line = fp.readline()
           
            except:
                # If the proxy ain't working out of the box, we don't need it
                    print(" " + ip + " is bad :(")
                    print (liner)
                    line = fp.readline()
                    cntr +=1
    return IPs, counter;

# storing all working proxies here
def writer():
    #print ("Loading up writer")
    
    IPs, counter = checker()
    # Time to get rid of the old proxies in the file and replace them with the ones that work
    f = open(filepath, "w")
    for element in IPs:
        f.write(element)
        f.write("\n")
    f.close()


    # and now we're done!
    print (liner2)
    print (" " + str(counter) + " proxies are working and have been stored in " + filepath)
    print (liner2)
    return;


writer()
