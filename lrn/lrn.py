#!/usr/bin/env python
import argparse
import sys
import os

from termcolor import colored, cprint

import subprocess
from subprocess import call, check_output, STDOUT

import api
import repl

l = api.l

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

    l('')

def introduce():
    """ Welcomes a new user to the {name} tutorial."""
    config = api.get_local_config()
    l(config['introduction'] + '\n', 'green')


def show_task():
    """ Informs the user of their current task."""
    task = api.get_task()
    l(task['instruction'] + '\n', 'cyan')



def start(name):
    url = 'https://github.com/lrn-guru/learn-{}.git'.format(name)
    # if there are no files, work here
    if len(check_output('ls -a'.split())) == 5:
        command = 'git clone {} .'.format(url)
    else:
        command = 'git clone {}'.format(url)
        l('Enter `cd learn-{} && lrn resume` to get started.'.format(name))
        exit(0)

    dev_null = open(os.devnull, 'w')
    call(command.split(), stdout=dev_null, stderr=subprocess.STDOUT)

    api.set_lrn_task(0)

    branch = api.get_starting_branch()
    command = 'git checkout {}'.format(branch)
    call(command.split(), stdout=dev_null, stderr=subprocess.STDOUT)
    introduce()
    show_task()
    start_repl()


def run_tests():
    # get the current branch
    task = api.get_task()
    test = task['test']

    print(test)
    # test_file =

def hint():
    task_json = api.get_task()
    print(task_json['hint'])

def start_repl():
    """
    Put the user into an interactive session where
    we can monitor their output. They exit with control d.
    cd into the right directory if possible.
    """
    repl.repl()



def progress():
    #displaying completed or incompleted lessons
    #get local config to parse:

    config = api.get_local_config()
    branch = api.get_branch()
    task = api.get_task()
    # get the highest lesson completed
    __import__('ipdb').set_trace()
    for index, lesson in enumerate(config['lessons']):
        if lesson['branch'] == branch:
            break

    for lesson in config['lessons']:
        index -= 1
        text = colored(lesson['name'], 'blue')
        if index > 0:
            print('  [x] ' + text)
        else:
            print('  [ ] ' + text)

        for i in range(len(lesson['tasks'])):
            text = colored(i, 'green')
            if i < task:
                print('\t[x] task ' + text)
            else:
                print('\t[ ] task ' + text)

def resume():
    show_task()
    repl.repl()

def next_task():
    # find how many tasks in this lesson
    config = api.get_local_config()
    branch = api.get_branch()
    for index, lesson in enumerate(config['lessons']):
        if lesson['branch'] == branch:
            break # we have the right lesson

    task_length = len(lesson['tasks'])
    task = api.get_lrn_task()
    if task < task_length:
        api.set_lrn_task(task + 1)
        show_task()
    else:
        congrats = lesson['completion']
        l(congrats, 'green')
        api.set_lrn_task(0)
        # stash changes
        call('git stash'.split(), stdout=open('/dev/null', 'w'), stderr=STDOUT)
        # get next branch
        next_branch = config['lessons'][index + 1]['branch']
        call('git checkout {}'.format(next_branch), stdout=open('/dev/null', 'w'), stderr=STDOUT)
        show_task()


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
    elif args.command == 'resume':
        resume()
    elif args.command == 'next':
        next_task()
    else:
        print('!')

if __name__ == '__main__':

    help_message = (
        'Available commands:\n\n'
        '\tlist     ----  Give a list of all available tutorials.\n'
        '\tstart    ----  Start a lesson.\n'
        '\tprogress ----  Display your lesson progress in a tutorial\n'
        '\thint     ----  Give a hint for the current problem\n'
        '\tresume   ----  Resume the tutorial after user exits\n'
        '\tnext     ----  Advance to the next lesson\n'
    )
    if (len(sys.argv) == 1):
        print(help_message)
        exit(0)
    description = 'lrn -- the interactive tutorial platform'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('command', help='The action to take (list, start, et cetera)')
    # parser.add_argument('-v', '--virtual', help='Whether or not to run lrn in a virtual machine')

    args, sub_args = parser.parse_known_args()
    main()
