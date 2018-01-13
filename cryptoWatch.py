import argparse

p = argparse.ArgumentParser(description="Small program for fetching crypto values")
p.add_argument("longform", metavar='Name', type=str, nargs='+', help="Expects the longform name of a cryptocurrency (\"Bitcoin\", not \"BTC\")")
a = p.parse_args()

def query(arr):

    #for i in range(0,len(arr)):

