import requests
import tqdm

API_URL = 'https://superheroapi.com/api/'
TOKEN = '2619421814940190'
heroes_names = ['Hulk', 'Captain America', 'Thanos']
powers = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']


def get_score_by_powers(heroes_names, powers):
    result = []
    for hero_name in tqdm.tqdm(heroes_names):
        response = requests.get(API_URL + TOKEN + '/search/' + hero_name)
        data = response.json()
        for hero in data['results']:
            if hero['name'] != hero_name:
                continue
            hero['score'] = 0
            for char in powers:
                hero['score'] += int(hero['powerstats'][char])
            result.append(hero)
    return result


heroes = get_score_by_powers(heroes_names, powers)

heroes.sort(key=lambda x: int(x['score']), reverse=True)

print(f'Самый сильный Супер Герой: {heroes[0]["name"]}. Набрал: {heroes[0]["score"]} очков')
