#!/usr/bin/env python
from __future__ import print_function

import argparse
import sys
import os

from termcolor import cprint

from subprocess import call

import api

def l(s, color=None, newline=True):
	''' Print a string with a color, no endline.'''
	opts = {'end': '\n' if newline else ''}
	if color:
		cprint(s, color, **opts)
	else:
		print(s, **opts)


description = 'lrn -- the interactive tutorial platform'
parser = argparse.ArgumentParser(description=description)

parser.add_argument('command', help='The action to take (list, start, et cetera)')
# parser.add_argument('-v', '--virtual', help='Whether or not to run lrn in a virtual machine')

args, sub_args = parser.parse_known_args()

projects = api.get_repos()


def list_projects():
	l('id'.ljust(9), 'white', False)
	l('description'.ljust(58), 'white', False)
	l('difficulty', 'white')
	l('-' * 73)
	for proj in projects:
		l(proj[0].ljust(9), 'yellow', False)
		l(proj[1].ljust(60), 'blue', False)
		l('*' * proj[2], 'yellow')

def introduce():
	""" Welcomes a new user to the {name} tutorial."""
	config = api.get_local_config()
	l(config['introduction'], 'green')


def task(number=None):
	""" Informs the user of their current task."""
	# If the task number is not none, ask the api for that
	task = api.get_task(number)
	l(task['instruction'], 'cyan')



def start(name):
	url = 'https://github.com/lrn-guru/learn-{}.git'.format(name)
	command = 'git clone {}'.format(url)
	call(command.split())
	folder = 'learn-{}'.format(name)
	os.system('cd {}'.format(folder))
	os.chdir(folder)
	os.system('export LRN_TASK=0')
	branch = api.get_starting_branch()
	command = 'git checkout {}'.format(branch)
	os.system(command)
	introduce()
	task()


def run_tests():
	# get the current branch
	task = api.get_task()
	test = task['test']

	print(test)
	# test_file =

def hint():
	task_json = api.get_task()
	print(task_json['hint'])


if args.command == 'list':
	list_projects()
elif args.command == 'start':
	if len(sys.argv) == 3:
		start(sys.argv[-1])
	else:
		l('Error: Specify a tutorial to start.', 'red')
elif args.command == 'hint':
	hint()
else:
	print('!')
