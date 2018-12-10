#Project started 10/12/2018
#BQAnon

import sys
import os

if len(sys.argv) == 1:
   print('Usage: python3 %s <input file>' % (sys.argv[0]))
   sys.exit(1)
hosts_open = open(sys.argv[1],'r')
hosts_read = hosts_open.readlines()
hosts_open.close()

#PS test
e = 0
while len(hosts_read) > e:
    command = 'python2 PRET/pret.py -i commands_pret.sh '+hosts_read[e].replace('\n',' ')+'ps'
    print('Ejecuting.... '+command)
    os.system(command)
    e += 1
