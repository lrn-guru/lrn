from distutils.core import setup

setup(
    name='lrn-guru',
    version='0.0.1',
    author=['Razzi Abuissa','Alex Brashear'],
    author_email='alexjbrashear@gmail.com',
    packages='lrn',
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)
