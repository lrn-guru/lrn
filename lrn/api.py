import requests
import json

def get_repos():
	r = requests.get('https://api.github.com/orgs/lrn-guru/repos')
	repos = r.json()
	repo_names = []
	for repo in repos:
		name = repo['full_name'].split('/')
		project_name = name[1].split('-')[1]
		j = get_config(project_name)
		description = j['short_description']
		difficulty = j['difficulty']
		repo_names.append(project_name, description, difficulty)

	return repo_names

def get_config(name):

	request = 'https://raw2.github.com/lrn-guru/learn-django/master/.config.json'
	#request = 'https://raw2.github.com/lrn-guru/learn-' + name + '/master/.config.json'
	r = requests.get(request)
	return r.json()


	
