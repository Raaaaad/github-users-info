import requests
import json
from flask import Flask
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
api_users_string = 'https://api.github.com/users'


@app.route('/repos/<username>')
@swag_from('./swagger-descriptions/list-repos.yml')
def list_repos(username):
    gh_request = requests.get(f'{api_users_string}/{username}/repos')
    if gh_request.status_code == 404:
        return 'User not found', 404
    json_response = json.loads(gh_request.text)
    user_repos = []
    for repo in json_response:
        name = repo['name']
        stars = repo['stargazers_count']
        user_repos.append({'name': name, 'stars': stars})

    return json.dumps(user_repos), 200


@app.route('/stars/<username>')
@swag_from('./swagger-descriptions/sum-stars.yml')
def sum_stars(username):
    gh_request = requests.get(f'{api_users_string}/{username}/repos')
    if gh_request.status_code == 404:
        return 'User not found', 404
    json_response = json.loads(gh_request.text)
    stars_sum = 0
    for repo in json_response:
        stars_sum += repo['stargazers_count']

    return json.dumps({'stars_sum': stars_sum}), 200


# https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting must be described in Readme +
# instructions how to generate GH token and use it within this app
@app.route('/languages/<username>')
@swag_from('./swagger-descriptions/languages-stats.yml')
def languages_stats(username):
    gh_request = requests.get(f'{api_users_string}/{username}/repos')
    if gh_request.status_code == 404:
        return 'User not found', 404
    json_response = json.loads(gh_request.text)
    languages = {}
    for repo in json_response:
        languages_url = repo['languages_url']
        language_stats = requests.get(languages_url)
        languages_dict = json.loads(language_stats.text)
        for key in languages_dict:
            if key in languages:
                languages[key] += languages_dict[key]
            else:
                languages[key] = languages_dict[key]

    return json.dumps(dict(sorted(languages.items(), key=lambda item: item[1]))), 200


if __name__ == '__main__':
    app.run(debug=True)
