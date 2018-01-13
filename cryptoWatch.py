import argparse
import json
import urllib

p = argparse.ArgumentParser(description="Small program for fetching crypto values")
p.add_argument("longform", metavar='name:amount', type=str, nargs='+', help="Expects the longform name of a cryptocurrency (\"Bitcoin\", not \"BTC\") followed by the amount you own")
arr = p.parse_args()



def query(crypto, fiat):


    url = "https://api.coinmarketcap.com/v1/ticker/{}/?convert={}".format(crypto, fiat)
    data = urllib.urlopen(url)
    readable = json.load(data)

    try:
        return readable[0]['price_{}'.format(fiat)]

    except KeyError:
        raise Exception("Invalid Cryptocurrency")
        return 1

print(query(getattr(arr,'longform')[0],'usd'))