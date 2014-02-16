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
        js = get_config(github_name)
        description = js['short_description']
        difficulty = js['difficulty']
        repo_names.append((github_name, description, difficulty))

    return repo_names

def get_local_config():
    if os.path.exists('.config.json'):
        path = ''
    elif os.path.exists('../.config.json'):
        path = '../'
    elif os.path.exists('../../.config.json'):
        path = '../../'
    else:
        print('You are not currently in a tutorial')
        return 1
    with open('{}.config.json'.format(path), 'r') as js:
        return loads(js.read())

def get_config(name):
    url = 'https://raw.github.com/lrn-guru/learn-{}/master/.config.json'.format(name)
    r = requests.get(url)
    return r.json()


def get_local_config():
    if os.path.exists('.config.json'):
        path = ''
    elif os.path.exists('../.config.json'):
        path = '../'
    else:
        path = '../../'
    with open('{}.config.json'.format(path), 'r') as js:
        return loads(js.read())


def get_task():
    branch = get_branch()
    config = get_local_config()
    for lesson in config['lessons']:
        if lesson['branch'] == branch:
            break # at the right lesson

    lrn_task = get_lrn_task()

    return lesson['tasks'][lrn_task]

def get_branch():
    status = check_output('git branch'.split())
    return status[2:status.find('\n')]

def get_starting_branch():
    config = get_local_config()
    return config['lessons'][0]['branch']

def find_lrn_txt():
    this_dir = '.lrn_task.txt'
    for i in range(4):
        path = '..' * i + this_dir
        if os.path.exists(path):
            return path

    # If it was not found, make it.
    return this_dir


def set_lrn_task(number):
    lrn_txt = find_lrn_txt()
    with open(lrn_txt, 'w') as f:
        f.write(str(number))

def get_lrn_task():
    lrn_txt = find_lrn_txt()
    with open(lrn_txt, 'r') as f:
        return int(f.read())
