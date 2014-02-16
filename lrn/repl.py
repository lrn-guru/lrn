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
        while True:
            import ipdb; ipdb.set_trace()
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

    except (EOFError, KeyboardInterrupt):
        print('Exiting lrn. Enter `lrn resume` to resume.')
        exit(0)



if __name__ == '__main__':
    repl()
