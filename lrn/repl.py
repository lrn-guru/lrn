from subprocess import check_output
import termios
import sys
import pty

def getpass(prompt="Password: "):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = raw_input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd

def main():
	while True:
		cmd = raw_input("> ")
		print(check_output(cmd.split()))


if __name__ == '__main__':
	#passw = getpass("> ")
	#print(passw)
	pty.spawn()
	

