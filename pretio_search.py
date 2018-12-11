#Project started: 08/12/2018 4:38
#BQAnon
#shodan_search.py

import shodan
import sys
import os
from io import open
from time import sleep

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[1;34m"
Y = "\033[1;33m"
W = "\033[1;37m"

os.system('')
print('%s## ## ## ## ##\n%s   PRET.IO\n%s## ## ## ## ##\n' % (W,G,W))
key_open = open('api_key.txt','r')
key_read = key_open.readlines()
ip = B+'# '
if len(key_read) == 0:
	print(R+'Error'+W+' can not find a key available.'+G)
	key_api = input('Enter you key: '+W)
	key_open2 = open('api_key.txt','w')
	key_open2.write(key_api)
	key_open2.close()
	api = shodan.Shodan(key_api)
elif len(key_read) == 1:
	api = shodan.Shodan(key_read[0])
else:
	print(warn+'Unexpect'+W+' error.')
if len(sys.argv) == 1:
	print('%sUsage: %spython3 ' % (G,W)+sys.argv[0]+' <query search>')
	sys.exit(1)
#try:
query = ' '.join(sys.argv[1:])
file_hosts = 'hosts.'+query+'.txt'
search = api.search(query)
i = 0
for service in search['matches']:
	sleep(0.25)
    #Info gather
	print(ip+W+' '+service['ip_str'])
	print(B,'  * ',W,'city',G,'   :',W,service['location']['city'])
	print(B,'  * ',W,'country',G,': ',W,service['location']['country_name'])
	print(B,'  * ',W,'port',G,'   : ',W,service['port'])
	i += 1
	hosts_open = open(file_hosts,'a+')
	hosts_open.write(service['ip_str']+'\n')
	hosts_open.close()
print('\n',G,i,W,'Results found.')
print(G+'Succes'+W+' saved in. '+file_hosts+'/')
#except Exception as e:
#	print('%sError %s%s' % (R,W,e))
#	sys.exit(1)
