Hello there, this is my own little repository with stuff that I made, mostly for myself.
As such, there isn't anything too crazy in here, mainly vanity stuff or some useful things for whatever I do.


# Trackify

This is a little bash script that shows what Spotify is playing in terminal, using SP.





# Proxer
![Proxer initial start](https://i.imgur.com/cZI50jb.png)

This program will fetch proxies, store them in a file and then check every every proxy within that file.
It does this by sending a GET request to the simple version of icanhazip via the proxy.
If the proxy is alive, it will be displayed as such and will be stored.

At the end of the checking operation, it will then overwrite the entire file with all working proxies.

This process is optional, you will be prompted if you would like to exit, after the intial fetching.

**Dependencies**
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
* Python 3 (might work in older versions, probably not tho)
* [Requests](https://requests.readthedocs.io/en/master/user/install/)



