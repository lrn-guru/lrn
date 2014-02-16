from distutils.core import setup

setup(
    name='lrn',
    version='0.2.2',
    author='Razzi Abuissa + Alex Brashear + Peter Yin',
    author_email='py.peteryin@gmail.com',
    url='https://github.com/lrn-guru',
    packages=['lrn'],
    scripts=['rlwrap', 'lrn/lrn', 'lrn/lrn.py', 'lrn/api.py', 'lrn/repl.py'],
    install_requires=[
        'requests==2.2.1',
        'termcolor==1.1.0'
    ]
)
