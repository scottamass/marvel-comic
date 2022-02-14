import requests
import hashlib
import datetime




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
params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params()}

def get_heros():
    
    all = requests.get(f'{baseurl}/characters',params=params).json()
    heros= all["data"]['results']
    return heros


def search_hero(search):    
    
    params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params()}
    response = requests.get(f'{baseurl}/characters?nameStartsWith={search}',params=params).json()
    hero=response["data"]['results']
    return hero
    #try:
    #    parsed_json = response
    #    name = parsed_json["data"]["results"][0]["name"]
    #    desc = parsed_json["data"]["results"][0]["description"]
    #    comics = parsed_json["data"]["results"][0]["comics"]['items']
    #    print(name)
    #    print(desc)
    #    for item in comics:
    #        print(item['name'])

    #except IndexError:
    #    print('not found')
def display_hero(characterId):
    params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params()}
    response= requests.get(f'{baseurl}/characters/{characterId}',params=params).json()
    results = response['data']['results']
    return results


def get_comics(characterId):
    params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params(), 'limit':50}
    response= requests.get(f'{baseurl}/characters/{characterId}/comics',params=params).json()
    comics = response['data']['results']
    return comics
    
def load_more(characterId):
    ofset = 50
    params = {'ts': timestamp, 'apikey': authPub, 'hash': hash_params(), 'ofset':ofset}
    response= requests.get(f'{baseurl}/characters/{characterId}/comics',params=params).json()
    comics = response['data']['results']
    ofset += ofset
    print(ofset)
    return comics
        