"""Main module."""
import json
from github_stats.cli import cli_args
from github_stats.auth.user import User
from github_stats.actions.users import Users
from github_stats.actions.repos import Repos


def main():
    """Main function."""

    args = cli_args()
    user = User(args)
    github_connection = user.auth()

    action_map = {'user-attrs': user_attrs, 'user-repos': user_repos}

    action = action_map[args.action]

    action(github_connection)


def user_attrs(github_connection):
    """Returns attribute information for user."""

    user = Users(github_connection)
    attrs = user.current_user_attrs()
    print(json.dumps(attrs))


def user_repos(github_connection):
    """Return user repos."""

    repos = Repos(github_connection)
    all_repos = repos.all()
    print(json.dumps(all_repos))


if __name__ == "__main__":
    main()
