#abrir e testar site

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO')
else:
    print('OK')