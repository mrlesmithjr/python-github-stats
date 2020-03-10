# python-github-stats

Just a little fun project to capture some stats for a users GitHub repos.

## Build Status

### GitHub Actions

![Python Test](https://github.com/mrlesmithjr/python-github-stats/workflows/Python%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/mrlesmithjr/python-github-stats.svg?branch=master)](https://travis-ci.org/mrlesmithjr/python-github-stats)

## Requirements

### GitHub API Personal Token

You will need to create a [GitHub API Personal Token](https://github.com/settings/tokens) in order to authenticate.

To use your token you will either need to use `--token PersonalAccessToken` or
create/edit a `~/.netrc`.

The `~/.netrc` file should look like:

```bash
machine github.com
password = PersonalAccessToken
machine api.github.com
password = PersonalAccessToken
```

- [requirements.txt](requirements.txt)
- [requirements-dev.txt](requirements-dev.txt)

## Dependencies

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-python-project](https://github.com/mrlesmithjr/cookiecutter-python-project) as a template.
