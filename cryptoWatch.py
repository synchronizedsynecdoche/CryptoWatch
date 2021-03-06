#!/usr/bin/env python

import argparse
import json
import urllib
from datetime import datetime

p = argparse.ArgumentParser(description="Small program for fetching crypto values")
p.add_argument('-f', '--fiat',metavar='fiat',type=str,default='usd', help="expects the shorthand ticker symbol for "
                                                                          "a fiat supported by coinmarketcap")
p.add_argument("longform", metavar='longform', type=str, nargs='+', help="Expects the name or symbol of a "
               "cryptocurrency (\"Bitcoin\" or  \"BTC\") followed by the amount you own")
arr = p.parse_args()
data = urllib.urlopen("https://api.coinmarketcap.com/v1/ticker/?convert={}&limit=0".format(arr.fiat))
r = json.load(data)

def query(crypto, fiat, readable):
    iterator = 0

    while True:
        try:
            try:
                readable[iterator]['price_{}'.format(fiat)]

            except KeyError:
                raise Exception("Invalid fiat")

            if readable[iterator]['id'] == crypto or readable[iterator]['name'] == crypto or readable[iterator]['symbol'] == crypto.upper():

                return float(readable[iterator]['price_{}'.format(fiat)])

            iterator += 1

        except IndexError or KeyError:
            raise Exception("Invalid cryptocurrency")


time = datetime.fromtimestamp(int(r[0]['last_updated'])).strftime('%m/%d/%Y %H:%M:%S')
print("Values updated at {}\n--------------------".format(time))

i = 0
sigma = 0
while True:

    try:
        x = arr.longform[i].split(":")[1]

    except IndexError:

        try:

            raise Exception("Invalid amount for {}".format(arr.longform)[i].upper().split(":")[0])

        except:  # end of the line
            pass

    try:

        amount = query(arr.longform[i].upper().split(":")[0],arr.fiat.lower(), r) * float(arr.longform[i].upper().split(":")[1])
        print(arr.longform[i].upper().split(":")[0] + " : " + str(amount))
        i += 1
        sigma += amount

    except IndexError:

        print("--------------------\nTotal : "+str(sigma))
        break

