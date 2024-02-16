from urllib.request import urlopen
import requests

from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urlparse

headers = {
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
}

#url = 'https://www.instagram.com/'
#url = 'https://retail.onlinesbi.sbi/retail/login.htm'
#url = 'https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fregion%2Feu%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsg-NDZQWQAa-reeTEQ2F-KWxwBlebnfQX7RshdIRM-Lk-AAAAAQAAAABlwlITcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Fregion%2Feu%2F%3Fref_%253Datv_auth_pre&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_in&openid.mode=checkid_setup&siteState=258-6829895-4399135&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

url = "http://www.coursera-account-verification.net/"

#hostname maathram kittaan...abs

hostname = urlparse(url).hostname
hostname = str(hostname)+"\n"
hostname2text = hostname

#Hostnameil ninn spl chars ozhivaakkaan...
spl_chars = [';', ':', '!', "*",'-','.']

'''
for i in spl_chars:
    hostname2text = hostname2text.replace(i, '')
    #print(hostname2text)
print(hostname2text)
'''
#_______________OR____________________________



# hostnamele . replace cheyth " "space add aaki nokknm....

hostname2text = hostname2text.replace('.',' ')
print(hostname2text)

try:

    response = requests.get(url,headers=headers)

    content = response.content

    data = BeautifulSoup(response.content,'html.parser')

    text = data.get_text()
    

    text = concat(hostname2text,text)
    print(text)
    #print("{} is looks like a legitimate page...".format(url))

    

except:
    #print("{} is looks like a phishing page...".format(url)) #----->Exact phishing aan soo ivde oru flag set chyth phisg_flag=True pinneed ath verify aakm..
    text = str(hostname2text)

with open("coursera/phish2.txt", "w", encoding="utf-8") as f:
    f.write(text)
    f.close()



