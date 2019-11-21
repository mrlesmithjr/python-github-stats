#!/usr/bin/env python

import json
from configparser import ConfigParser
from github import Github, GithubException

PARSER = ConfigParser()
PARSER.read('github.cfg')

# Parse github.cfg file to get user and token
GH_USER = PARSER.get('github', 'user')
GH_USER_TOKEN = PARSER.get('github', 'token')

# Instantiate GitHub connection
GH = Github(GH_USER, GH_USER_TOKEN)

# Get all of users repos
USER_REPOS = GH.get_user().get_repos()

# Define initial REPOS dictionary
REPOS = dict(open=dict(issues=dict(), pull_requests=dict()),
             top=dict(clones=dict(), views=dict()), all=dict())

# Defines the number of top clones, views that you are interested in
TOP_COUNT = 10

# Iterate through users repos
for repo in USER_REPOS:
    repo_info = GH.get_repo(repo.full_name)
    try:
        topics = repo_info.get_topics()
        stargazers_count = repo_info.stargazers_count

        issues = list()
        open_issues = repo_info.get_issues(state='open')
        for issue in open_issues:
            issue_info = dict(title=issue.title, number=issue.number)
            issues.append(issue_info)
        if issues != []:
            REPOS['open']['issues'][repo.name] = issues

        pull_requests = list()
        for pull_request in repo_info.get_pulls(state='open'):
            pull_request_info = dict(
                title=pull_request.title, number=pull_request.number)
            pull_requests.append(pull_request_info)
        if pull_requests != []:
            REPOS['open']['pull_requests'][repo.name] = pull_requests

        clone_traffic = repo.get_clones_traffic(per="week")
        REPOS['top']['clones'][repo.name] = dict(
            clones=clone_traffic['count'])

        weekly_clones = list()
        for clone in clone_traffic['clones']:
            clone_info = dict(count=clone.count,
                              timestamp=str(clone.timestamp),
                              uniques=clone.uniques)
            weekly_clones.append(clone_info)

        view_traffic = repo_info.get_views_traffic(per='week')

        REPOS['top']['views'][repo.name] = dict(
            views=view_traffic['count'])

        weekly_views = list()
        for view in view_traffic['views']:
            view_info = dict(count=view.count,
                             timestamp=str(view.timestamp),
                             uniques=view.uniques)
            weekly_views.append(view_info)

        top_referrers = list()
        for referrer in repo_info.get_top_referrers():
            referer_info = dict(count=referrer.count,
                                referrer=referrer.referrer,
                                uniques=referrer.uniques)
            top_referrers.append(referer_info)

        top_paths = list()
        for path in repo_info.get_top_paths():
            path_info = dict(count=path.count,
                             path=path.path, uniques=path.uniques)
            top_paths.append(path_info)

        REPOS['all'][repo.name] = dict(
            clones=weekly_clones, open_issues=issues,
            pull_requests=pull_requests,
            top_referrers=top_referrers, top_paths=top_paths,
            stars=stargazers_count, topics=topics, views=weekly_views)

    except GithubException:
        pass

# Sort by top clones
REPOS['top']['clones'] = dict(sorted(REPOS['top']['clones'].items(),
                                     key=lambda x: x[1]['clones'],
                                     reverse=True)[:TOP_COUNT])

# Sort by top views
REPOS['top']['views'] = dict(sorted(REPOS['top']['views'].items(),
                                    key=lambda x: x[1]['views'],
                                    reverse=True)[:TOP_COUNT])

# Write REPOS dictionary to JSON file
with open('repo_stats.json', 'w') as results:
    json.dump(REPOS, results, indent=4)
