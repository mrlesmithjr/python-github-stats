"""Provides the GitHub Users class."""

import json


class Users:
    """Main GitHub User class."""

    def __init__(self, github_connection):
        """Init a thing"""

        self.github_connection = github_connection

    def current_user_attrs(self):
        """Retrieves current users attributes and returns them."""

        # Define current user based on API connection
        current_user = self.github_connection.get_user()

        json_raw_data = json.dumps(current_user.raw_data)
        current_user_attrs = json.loads(json_raw_data)

        return current_user_attrs
