"""Provides the user Repos class."""
import json


class Repos():
    """Main GitHub Repos class."""

    def __init__(self, github_connection):
        """Init a thing"""

        self.github_connection = github_connection
        self.repos = {}

    def all(self):
        """Get all of the users repos and return."""

        user = self.github_connection.get_user()
        repos = user.get_repos()

        for repo in repos:
            raw_data = json.dumps(repo.raw_data)
            self.repos[repo.full_name] = json.loads(raw_data)

            self.get_issues(repo)
            self.get_pulls(repo)
            self.get_top_referrers(repo)
            self.get_clones_traffic(repo)
            self.get_views_traffic(repo)

            break

        return self.repos

    def get_issues(self, repo):
        """Get list of issues for repo and append to self.repos dict."""

        issues = []
        open_issues = repo.get_issues()
        for issue in open_issues:
            raw_data = json.dumps(issue.raw_data)
            issues.append(json.loads(raw_data))

        self.repos[repo.full_name]['issues'] = issues

    def get_pulls(self, repo):
        """Get list of pull requests for repo and append to self.repos dict."""

        pull_requests = []
        pulls = repo.get_pulls()
        for pull in pulls:
            raw_data = json.dumps(pull.raw_data)
            pull_requests.append(json.loads(raw_data))

        self.repos[repo.full_name]['pulls'] = pull_requests

    def get_top_referrers(self, repo):
        """Get list of top referrers for repo and append to self.repos dict."""

        top_referrers = []
        referrers = repo.get_top_referrers()
        for referrer in referrers:
            raw_data = json.dumps(referrer.raw_data)
            top_referrers.append(json.loads(raw_data))

        self.repos[repo.full_name]['top_referrers'] = top_referrers

    def get_clones_traffic(self, repo):
        """Get clone traffic for repo and append to self.repos dict."""

        clones = repo.get_clones_traffic()

        self.repos[repo.full_name]['clones_traffic'] = {
            'count': clones['count'], 'uniques': clones['uniques'],
            'clones': clones['clones']}

    def get_views_traffic(self, repo):
        """Get view traffic for repo and append to self.repos dict."""

        views = repo.get_views_traffic()

        self.repos[repo.full_name]['views_traffic'] = {
            'count': views['count'], 'uniques': views['uniques']}
