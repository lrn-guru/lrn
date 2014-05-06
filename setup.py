from setuptools import setup, find_packages

setup(
    name='lrn',
    version='0.2.6',
    author='Razzi Abuissa + Alex Brashear + Peter Yin',
    author_email='py.peteryin@gmail.com',
    url='https://github.com/lrn-guru',
    packages=find_packages(),
    install_requires=[
        'requests==2.2.1',
        'termcolor==1.1.0'
    ],
    entry_points={
        'console_scripts': [
            'lrn=lrn.lrn:main'
        ]
    }
)
