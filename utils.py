import json

import requests


def get_languages(raw_json):
    languages_url = raw_json['languages_url']
    language_stats = requests.get(languages_url)
    languages_dict = json.loads(language_stats.text)
    return languages_dict
