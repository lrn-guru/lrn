#!/usr/bin/env python
from __future__ import print_function

import argparse
import sys
import os

from termcolor import colored, cprint

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


def task():
	""" Informs the user of their current task."""
	task = api.get_task()
	l(task, 'blue')



def start(name):
	url = 'https://github.com/lrn-guru/learn-{}.git'.format(name)
	command = 'git clone {}'.format(url)
	call(command.split())
	folder = "learn-{}".format(name)
	os.chdir(folder)
	os.environ['LRN_TASK'] = '0'
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

def progress():
	#displaying completed or incompleted lessons
	#get local config to parse:

	############# set up progress report #######################
	l('-' * 73)
	cprint('Progress Report: \n\n', 'cyan')
	word = colored('  Complete:   ', 'cyan')
	c_text = colored('   ', 'green', attrs=['reverse', 'blink'])
	print(word + '[' + c_text + ']')

	word = colored('  Incomplete: ', 'cyan')
	i_text = colored('   ', 'red', attrs=['reverse', 'blink'])
	print(word + '[' + i_text + ']\n')
	############# end set up              ######################

	full_local_config = api.get_local_config()
	if full_local_config == 1:
		return
	else:
		for j in full_local_config['lessons']:
			text = colored(j['name'], 'blue')
			print('  [' + i_text + ']: ' + text)
		print('\n')

def main():
	if args.command == 'list':
		list_projects()
	elif args.command == 'start':
		if len(sys.argv) == 3:
			start(sys.argv[-1])
		else:
			l('Error: Specify a tutorial to start.', 'red')
	elif args.command == 'hint':
		hint()
	elif args.command == 'progress':
		progress()
	else:
		print('!')

if __name__ == '__main__':
	main()




	