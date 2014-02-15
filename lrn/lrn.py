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

def introduce(name):
	""" Welcomes a new user to the {name} tutorial."""
	config = api.get_config(name)
	__import__('ipdb').set_trace()
	l(config['intruduction'], 'green')


def task():
	""" Informs the user of their current task."""
	task = api.get_task()
	l(task, 'blue')



def start(name):
	url = 'https://github.com/lrn-guru/learn-{}.git'.format(name)
	command = 'git clone {}'.format(url)
	call(command.split())
	call('cd {}'.format(name).split())
	os.environ['LRN_TASK'] = '1'
	introduce(name)
	task()


def run_tests():
	# get the current branch
	task = api.get_task()
	test = task['test']

	print(test)
	# test_file =


if args.command == 'list':
	list_projects()
elif args.command == 'start':
	# hackish
	if len(sys.argv) == 3:
		start(sys.argv[-1])
	else:
		l('Error: Specify a tutorial to start.', 'red')

else:
	print('!')
