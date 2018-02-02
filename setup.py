from setuptools import find_packages, setup

print()

version = '0.0.1a2'

setup(name='pawt',
      description='Pre-alpha Telegram API wrapper',
      install_requires=['requests >= 2.18.4'],
      packages=find_packages(exclude=['tests', 'tests.*']),
      version=version)
