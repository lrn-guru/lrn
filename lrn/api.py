import requests
import json

def get_repos():
	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
	repos = r.json()
	repo_names = []
	for repo in repos:
		name = repo['full_name'].split('/')
		j = get_config(name[1])
		description = j['short_description']
		difficulty = j['difficulty']
		repo_names.append(name[1], description, difficulty)

	return repo_names

def get_config(name):

	request = 'https://raw2.github.com/lrn-guru/' + name + '/master/.config.json'
	r = requests.get(request)
	return r.json()


	
