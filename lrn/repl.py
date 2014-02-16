import os

import api

l = api.l

from subprocess import check_output

def check_progress(cmd):
    task = api.get_task()
    test = task['test']
    test_dir = api.get_tests_dir()

    command = 'python {}/{}.py'.format(test_dir, test)
    status = check_output(command.split())
    return status

def repl():
    try:
        # os.environ['OLD_PS1'] = os.environ['PS1']
        # os.environ['PS1'] = 'lrn: ' + os.environ['PS1']
        while True:
            l('lrn ', 'cyan', False)
            l('> ', 'blue', False)
            cmd = raw_input('')
            if 'cd ' in cmd:
                folder = cmd[3:]
                os.chdir(folder)
            else:
                os.system(cmd)
            outcome = check_progress(cmd)
            print("REPL DEBUG")
            __import__('ipdb').set_trace()
            if outcome == "0":
                api.next()


    except EOFError:
        print('Exiting lrn...')
        exit(0)
        # os.environ['PS1'] = os.environ['OLD_PS1']



if __name__ == '__main__':
    repl()
