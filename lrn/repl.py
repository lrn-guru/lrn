import os


def main():
	try:
		# os.environ['OLD_PS1'] = os.environ['PS1']
		# os.environ['PS1'] = 'lrn: ' + os.environ['PS1']
		while True:
			cmd = raw_input("lrn > ")
			if cmd.startswith('vim'):
				os.system(cmd)
			else:
				print('enter vim')
	except EOFError:
		print('Exiting lrn...')
		exit(0)
		# os.environ['PS1'] = os.environ['OLD_PS1']



if __name__ == '__main__':
	main()


