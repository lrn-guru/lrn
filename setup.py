from distutils.core import setup

setup(
    name='lrn',
    version='0.1.3',
    author='Razzi Abuissa + Alex Brashear + Peter Yin',
    author_email='py.peteryin@gmail.com',
    url='https://github.com/lrn-guru',
    packages=['lrn'],
    scripts=['lrn/lrn', 'lrn/lrn.py', 'lrn/api.py', 'lrn/repl.py'],
)
