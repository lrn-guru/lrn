from distutils.core import setup

setup(
    name='lrn',
    version='0.1.0',
    author='Razzi Abuissa + Alex Brashear + Peter Yin',
    author_email='py.peteryin@gmail.com',
    url='https://github.com/lrn-guru',
    packages=['lrn', 'lrn.api', 'lrn.repl'],
    scripts=['lrn/lrn'],
)

