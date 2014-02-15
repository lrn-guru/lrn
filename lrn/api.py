import os
from subprocess import check_output

import requests
from pygit2 import Repository

def get_current_repo():
	if os.path.exists('.git'):
		return Repository('.')
	elif os.path.exists('../.git'):
		return Repository('..')
	elif os.path.exists('../../.git'):
		return Repository('../..')
	else:
		print('No git repository found.')
		exit(1)

def get_repos():
	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
	repos = r.json()
	repo_names = []
	for repo in repos:
		name = repo['full_name'].split('/')
		project_name = name[1]
		github_name = project_name[6:]
		j = get_config(github_name)
		description = j['short_description']
		difficulty = j['difficulty']
		repo_names.append((github_name, description, difficulty))

	return repo_names

def get_config(name):
	url = 'https://raw.github.com/lrn-guru/learn-{}/master/.config.json'.format(name)
	r = requests.get(url)
	return r.json()

def get_current_branch(repo):
	head = repo.listall_branches()[0]
	if head.is_head():
		return head
	else:
		print('locating current branch')
		status = check_output('git branch'.split())
		return repo.lookup_branch(status.split()[2])
