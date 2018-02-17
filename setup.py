from setuptools import find_packages, setup

from pawt import __version__

setup(name='pawt',
      description='Pre-alpha Telegram API wrapper',
      install_requires=['requests >= 2.18.4'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      test_suite='tests',
      packages=find_packages(exclude=['tests', 'tests.*']),
      version=__version__)
