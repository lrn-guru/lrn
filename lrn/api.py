import requests
import json

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
	
