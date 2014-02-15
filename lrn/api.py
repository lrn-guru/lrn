import os
from json import loads
from subprocess import check_output

import requests

def get_current_repo():
	if os.path.exists('.git'):
	# 	return Repository('.')
	# elif os.path.exists('../.git'):
	# 	return Repository('..')
	# elif os.path.exists('../../.git'):
	# 	return Repository('../..')
	# else:
		print('No git repository found.')
		exit(1)

def get_repos():
	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
	repos = r.json()
	# repos = loads(open('~/repos.json', 'r').read())
	repo_names = []
	for repo in repos:
		name = repo['full_name'].split('/')
		project_name = name[1]
		github_name = project_name[6:]
		j = get_config(github_name)
		description = j['short_description']
		difficulty = j['difficulty']
		print(preject_name)
		repo_names.append((github_name, description, difficulty))

	return repo_names

def get_local_config():
	if os.path.exists('.config.json'):
		with open('.config.json', 'r') as j:
			return loads(j.read())

def get_config(name):
	try:
		get_local_config(name)
	except Exception:
		url = 'https://raw.github.com/lrn-guru/learn-{}/master/.config.json'.format(name)
		r = requests.get(url)
		return r.json()

def get_current_branch():
	status = check_output('git branch'.split())
	return status.split()[2]
