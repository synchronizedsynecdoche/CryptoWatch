#!/usr/bin/env python
import argparse
import json
import urllib

p = argparse.ArgumentParser(description="Small program for fetching crypto values")

p.add_argument('-f', '--fiat',metavar='fiat',type=str,default='usd', help="expects the shorthand ticker symbol for a fiat"
                                                                 "supported by coinmarketcap")

p.add_argument("longform", metavar='longform', type=str, nargs='+', help="Expects the name or symbol of a "
               "cryptocurrency (\"Bitcoin\" or  \"BTC\") followed by the amount you own")

arr = p.parse_args()


def query(crypto, fiat):

    # give the option of grabbing straight from this link for less than 10 coins
    # url = "https://api.coinmarketcap.com/v1/ticker/{}/?convert={}".format(crypto, fiat)
    url = "https://api.coinmarketcap.com/v1/ticker/?convert={}&limit=0".format(fiat)
    data = urllib.urlopen(url)
    readable = json.load(data)

    iterator = 0
    while True:
        try:
            if readable[iterator]['id'] == crypto or readable[iterator]['name'] == crypto or readable[iterator]['symbol'] == crypto.upper():
                return float(readable[iterator]['price_{}'.format(fiat)])
            iterator += 1

        except IndexError or KeyError:
            raise Exception("Invalid cryptocurrency or fiat currency")


iterator = 0
sigma = 0
while True:

    try:
        x = getattr(arr,'longform')[iterator].split(":")[1]
    except IndexError:
        try:
            raise Exception("Invalid amount for {}".format(getattr(arr,'longform')[iterator].upper().split(":")[0]))
        except: # end of the line
            pass
    try:
	amount = query(arr.longform[iterator].upper().split(":")[0],arr.fiat.lower()) * float(arr.longform[iterator].upper().split(":")[1])

        print(arr.longform[iterator].upper().split(":")[0] +" : "+str(amount))
        iterator += 1
	sigma += amount
    except IndexError:
        print("Total : "+str(sigma))
	break
	
