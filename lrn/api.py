import os
from json import loads
from subprocess import check_output

# from ipdb import set_trace

import requests

def get_repos():
	# set_trace()
	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
	repos = r.json()
	# repos = loads(open('~/repos.json', 'r').read())
	repo_names = []
	for repo in repos:
		name = repo['full_name'].split('/')
		project_name = name[1]
		if (project_name == 'lrn' or project_name == 'lrn-guru.github.io'):
			continue
		github_name = project_name[6:]
		j = get_config(github_name)
		description = j['short_description']
		difficulty = j['difficulty']
		repo_names.append((github_name, description, difficulty))

	return repo_names

def get_local_config():
	if os.path.exists('.config.json'):
		path = ''
	elif os.path.exists('../.config.json'):
		path = '../'
	else:
		path = '../../'
	with open('{}.config.json'.format(path), 'r') as j:
		return loads(j.read())

def get_config(name):
	url = 'https://raw.github.com/lrn-guru/learn-{}/master/.config.json'.format(name)
	r = requests.get(url)
	return r.json()

def get_task():

	branch = get_branch()
	config = get_local_config()
	for lesson in config['lessons']:
		if lesson['branch'] == branch:
			break # at the right lesson

	lrn_task = os.environ['LRN_TASK']

	return lesson[lrn_task]

def get_branch():
	#import ipdb; ipdb.set_trace()
	status = check_output('git branch'.split())
	return status[2:].strip("\n")
