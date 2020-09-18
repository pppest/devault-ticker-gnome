#!/usr/bin/python
import urllib2
import json

#setings
FIAT = ["mxn","usd","btc"]
DECIMALS = 8
ICON = True

for f in FIAT:
    url2 = "https://api.coingecko.com/api/v3/simple/price?ids=devault&vs_currencies="+f
    result = urllib2.urlopen(url2).read()
    json_data = json.loads(result)
    coin_price = json_data['devault'][f]
    if ICON:
        print("DVT/"+f.upper()+" "+str(round(coin_price,DECIMALS))+" | iconName=devault-128")
    else:
        print("DVT/"+f.upper()+" "+str(round(coin_price,DECIMALS)))
