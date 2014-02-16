import os

import api
import lrn

l = api.l

from subprocess import call

def check_progress(cmd):
    task = api.get_task()
    test = task['test']
    test_dir = api.get_tests_dir()

    command = "python {}/{}.py {}".format(test_dir, test, cmd)
    status = call(command.split())
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
            if outcome == 0:
                lrn.next_task()


    except EOFError:
        print('Exiting lrn...')
        exit(0)
        # os.environ['PS1'] = os.environ['OLD_PS1']



if __name__ == '__main__':
    repl()
