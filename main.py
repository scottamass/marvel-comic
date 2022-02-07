from sqlite3 import Timestamp
import requests
import hashlib
import datetime

from pprint import pprint as pp
timestamp= datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
authPub="f2c645519a3fbb515476990b9992eb9d"
authPriv="cce38df6ee68a724906f282645263593aaf9003f"
baseurl="https://gateway.marvel.com:443/v1/public"

def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{authPriv}{authPub}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params
char="thor"
params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params()}
res = requests.get(f'{baseurl}/characters?name={char}',params=params)

results = res.json()
pp(results)