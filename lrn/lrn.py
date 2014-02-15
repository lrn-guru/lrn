#!/usr/bin/env python

import argparse

from termcolor import cprint

description = 'lrn -- the interactive tutorial platform'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-v', '--virtual', help='Whether or not to run lrn in a virtual machine')
parser.add_argument('command', help='The action to take (list, start, et cetera)')

args = parser.parse_args()
projects = [
	('django', 'An Introduction to Django', 2)
]

def list_projects():
	for proj in projects:
		cprint(proj[0].ljust(6), 'yellow', endline='')

if args.command == 'list':
	list_projects()
else:
	print('!')
