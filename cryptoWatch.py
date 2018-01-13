import argparse
import json
import urllib

p = argparse.ArgumentParser(description="Small program for fetching crypto values")
p.add_argument("longform", metavar='name:amount', type=str, nargs='+', help="Expects the longform name of a cryptocurrency (\"Bitcoin\", not \"BTC\") followed by the amount you own")
arr = p.parse_args()



def query(crypto, fiat):

    # give the option of grabbing straight from this link for less than 10 coins
    #url = "https://api.coinmarketcap.com/v1/ticker/{}/?convert={}".format(crypto, fiat)
    url = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
    data = urllib.urlopen(url)
    readable = json.load(data)

    iter = 0
    while True:
        try:
            if(readable[iter]['id'] == crypto or readable[iter]['name'] == crypto or readable[iter]['symbol'] == crypto.upper()):
                return readable[iter]['price_{}'.format(fiat)]
            iter += 1
        except IndexError:
            raise Exception("Invalid Cryptocurrency")

    return 1

iter = 0
while True:

    try:
        print(query(getattr(arr,'longform')[iter].split(":")[0],'usd'))
        iter += 1
    except IndexError:
        break