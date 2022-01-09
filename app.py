import requests
import json
from flask import Flask, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from GitHubRepository import GitHubRepository
from utils import get_languages

app = Flask(__name__)
swagger = Swagger(app)
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
        user_repository = GitHubRepository(repo)
        user_repos.append(user_repository.serialize())
    return jsonify(user_repos), 200


@app.route('/stars/<username>')
@swag_from('./swagger-descriptions/sum-stars.yml')
def sum_stars(username):
    gh_request = requests.get(f'{api_users_string}/{username}/repos')
    if gh_request.status_code == 404:
        return 'User not found', 404
    json_response = json.loads(gh_request.text)
    stars_sum = 0
    for repo in json_response:
        user_repository = GitHubRepository(repo)
        stars_sum += user_repository.get_stars_count()

    return json.dumps({'stars_sum': stars_sum}), 200


@app.route('/languages/<username>')
@swag_from('./swagger-descriptions/languages-stats.yml')
def languages_stats(username):
    gh_request = requests.get(f'{api_users_string}/{username}/repos')
    if gh_request.status_code == 404:
        return 'User not found', 404
    json_response = json.loads(gh_request.text)
    languages = {}
    for repo in json_response:
        repo_languages = get_languages(repo)
        for key in repo_languages:
            if key in languages:
                languages[key] += repo_languages[key]
            else:
                languages[key] = repo_languages[key]

    return json.dumps(dict(sorted(languages.items(), key=lambda item: item[1]))), 200


if __name__ == '__main__':
    app.run(debug=True)
