"""Console script for python-github-stats."""

import argparse
import os


def cli_args():
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description='Manage GitHub via API.')

    parser.add_argument(
        'action', help='Define action to take.', choices=[
            'user-attrs',
            'user-repos'])

    parser.add_argument('--netrcfile', help='Path to Netrc file',
                        default=os.path.join(
                            os.path.expanduser('~'), '.netrc'))
    parser.add_argument('--token', help='Your GitHub API private token.')
    parser.add_argument('--url', help='GitHub API url',
                        default='https://api.github.com')

    args = parser.parse_args()

    return args
