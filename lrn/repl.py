import os

def main():
	while True:
		cmd = raw_input("> ")
		if cmd.startswith('vim'):
			os.system(cmd)
		else:
			print('enter vim')


if __name__ == '__main__':
	main()
	

