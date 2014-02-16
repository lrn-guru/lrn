from distutils.core import setup

setup(
    name='lrn-guru',
    version='0.0.3',
    author='Razzi Abuissa + Alex Brashear',
    author_email='alexjbrashear@gmail.com',
    packages=['lrn'],
    scripts=['bin/lrn.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='The command line interface for the lrn tutorial platform',
    long_description=open('README.md').read(),
	install_requires=[],
    entry_points={
        'console_scripts': [
            'lrn = lrn.lrn:main',
        ],
    },
)

