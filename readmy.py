import requests
import json

def comparison_hero(link, hero_list):
    uri = link + '/all.json'
    responce = requests.get(uri)
    dict_local = {}
    for hero in json.loads(responce.text):
        for name_hero in hero_list:
            if name_hero == hero['name']:
                dict_local[hero['powerstats']['intelligence']] = hero['name']
            else:
                continue
    
    intl, name = sorted(dict_local.items())[-1]

    return print(f'Самый умный супергерой в этом списке согласно нашим данным - {name}, показатель его ума составляет - {intl}')


comparison_hero('https://akabab.github.io/superhero-api/api', ['Thanos', 'Hulk', 'Captain America'])