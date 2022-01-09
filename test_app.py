import pytest

from GitHubRepository import GitHubRepository
from utils import get_languages


@pytest.mark.parametrize("raw_json",
                         [
                             {
                                 "name": "repo1",
                                 "stargazers_count": 11
                             }
                         ])
def test_repos(raw_json):
    github_repository = GitHubRepository(raw_json)
    assert github_repository.name == raw_json["name"]
    assert github_repository.stars_count == raw_json["stargazers_count"]


@pytest.mark.parametrize("raw_json",
                         [
                             {
                                 "languages_url": "https://api.github.com/repos/Raaaaad/github-users-info/languages"
                             }
                         ])
def test_languages(raw_json):
    languages = get_languages(raw_json)
    assert languages['Python'] > 1000
