#!/usr/bin/env python

from __future__ import print_function
import argparse

from termcolor import cprint

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

args = parser.parse_args()
projects = [
	('django', 'An Introduction to Django', 2),
	('node', 'Writing a simple node.js server', 2),
	('ruby', 'Scripting with Ruby', 1),
	('gulp', 'Running node.js tasks with Gulp', 2),
	('go', 'Hello World in Go', 1),
	('sh', 'Shell scripting basics', 1),
	('ec2', 'Creating a custom AWS Elastic Compute Cloud (EC2) image', 3),
]

def list_projects():
	l('id'.ljust(9), 'white', False)
	l('description'.ljust(58), 'white', False)
	l('difficulty', 'white')
	l('-' * 73)
	for proj in projects:
		l(proj[0].ljust(9), 'yellow', False)
		l(proj[1].ljust(60), 'blue', False)
		l('*' * proj[2], 'yellow')

if args.command == 'list':
	list_projects()
else:
	print('!')
