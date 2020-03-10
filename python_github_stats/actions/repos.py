"""Provides the user Repos class."""
import json


class Repos():
    def __init__(self, github_connection):
        self.github_connection = github_connection

        self.repos = {}

    def all(self):
        user = self.github_connection.get_user()
        repos = user.get_repos()

        for repo in repos:
            json_raw_data = json.dumps(repo.raw_data)
            self.repos[repo.full_name] = json.loads(json_raw_data)

        return self.repos
