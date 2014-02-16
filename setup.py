from distutils.core import setup

setup(
    name='lrn',
    version='0.0.4',
    author='Razzi Abuissa + Alex Brashear + Peter Yin',
    author_email='py.peteryin@gmail.com',
    packages=['lrn'],
    url='https://github.com/lrn-guru/lrn',
    license='LICENSE.txt',
    description='The command line interface for the lrn tutorial platform',
    long_description= open('README.txt').read(),
	install_requires=[],
    entry_points={
        'console_scripts': [
            'lrn = lrn.lrn:main',
        ],
    },
)

