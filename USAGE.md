# Usage

This guide shows some of the various usages of using this project. Functionality
will change over time. So, this is just a subset of use cases.

## Help

```bash
python -m github_stats --help
...
usage: __main__.py [-h] [--netrcfile NETRCFILE] [--token TOKEN] [--url URL]
                   {user-attrs,user-repos}

Manage GitHub via API.

positional arguments:
  {user-attrs,user-repos}
                        Define action to take.

optional arguments:
  -h, --help            show this help message and exit
  --netrcfile NETRCFILE
                        Path to Netrc file
  --token TOKEN         Your GitHub API private token.
  --url URL             GitHub API url
```

## Repos

To get a list of all of your repositories:

```bash
python -m github_stats user-repos
```

## User

To view your GitHub user attributes:

```bash
python -m github_stats user-attrs
```
