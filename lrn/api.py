import requests
import os

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
		repo_names.append(name[1])

	return repo_names

def get_config(name):

	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
