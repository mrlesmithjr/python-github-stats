"""Provides the user Repos class."""
import json


class Repos():
    """Main GitHub Repos class."""

    def __init__(self, github_connection):
        """Init a thing"""

        self.github_connection = github_connection
        # Define repos dictionary
        self.repos = {}

    def all(self):
        """Get all of the users repos and return."""

        user = self.github_connection.get_user()
        # Get list of all repos for user
        repos = user.get_repos()

        # Iterate through all repos returned
        for repo in repos:
            # Define the raw data to dump/load the JSON
            raw_data = json.dumps(repo.raw_data)
            self.repos[repo.full_name] = json.loads(raw_data)

            # Get issues for repo
            self.get_issues(repo)
            # Get pull requests for repo
            self.get_pulls(repo)
            # Get top referrers for repo
            self.get_top_referrers(repo)
            # Get cloning traffic for repo
            self.get_clones_traffic(repo)
            # Get views traffic for repo
            self.get_views_traffic(repo)

        # Return all repos found with info as dictionary
        return self.repos

    def get_issues(self, repo):
        """Get list of issues for repo and append to self.repos dict."""

        # Define issues list
        issues = []
        # Get all issues open/closed for repo
        all_issues = repo.get_issues()
        # Iterate over all issues
        for issue in all_issues:
            # Define the raw data to dump/load the JSON
            raw_data = json.dumps(issue.raw_data)
            issues.append(json.loads(raw_data))

        # Update repo with issues
        self.repos[repo.full_name]['issues'] = issues

    def get_pulls(self, repo):
        """Get list of pull requests for repo and append to self.repos dict."""

        # Define pull requests list
        pull_requests = []
        # Get all pull requests open/closed for repo
        pulls = repo.get_pulls()
        # Iterate over all pulls
        for pull in pulls:
            # Define the raw data to dump/load the JSON
            raw_data = json.dumps(pull.raw_data)
            pull_requests.append(json.loads(raw_data))

        # Update repo with pull requests
        self.repos[repo.full_name]['pulls'] = pull_requests

    def get_top_referrers(self, repo):
        """Get list of top referrers for repo and append to self.repos dict."""

        # Define top referrers list
        top_referrers = []
        # Get top referrers for repo
        referrers = repo.get_top_referrers()
        # Iterate over top referrers
        for referrer in referrers:
            # Define the raw data to dump/load the JSON
            raw_data = json.dumps(referrer.raw_data)
            top_referrers.append(json.loads(raw_data))

        # Update repo with top referrers
        self.repos[repo.full_name]['top_referrers'] = top_referrers

    def get_clones_traffic(self, repo):
        """Get clone traffic for repo and append to self.repos dict."""

        # Get clones traffic for repo
        clones = repo.get_clones_traffic()

        # Update repos with clone traffic
        self.repos[repo.full_name]['clones_traffic'] = {
            'count': clones['count'], 'uniques': clones['uniques'],
            'clones': clones['clones']}

    def get_views_traffic(self, repo):
        """Get view traffic for repo and append to self.repos dict."""

        # Get views traffic for repo
        views = repo.get_views_traffic()

        # Update repo with view traffic
        self.repos[repo.full_name]['views_traffic'] = {
            'count': views['count'], 'uniques': views['uniques']}
