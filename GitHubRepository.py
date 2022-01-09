class GitHubRepository:
    def __init__(self, raw_json):
        self.name = raw_json["name"]
        self.stars_count = raw_json["stargazers_count"]

    def get_name(self):
        return self.name

    def get_stars_count(self):
        return self.stars_count

    def serialize(self):
        return {"name": self.name,
                "stars_count": self.stars_count
                }
