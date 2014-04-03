# -*- coding: utf-8 -*-
from __future__ import with_statement
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path


SETUP_DIR = os.path.dirname(__file__)


def read_file(path):
    path = os.path.join(SETUP_DIR, path)
    with file(path) as f:
        return f.read()


setup_info = {
    'name': 'myapp',
    'version': read_file('VERSION.txt').strip(),
    'description': '',
    'long_description': read_file('README.rst'),

    'author': 'mete0r',
    'author_email': 'mete0r@sarangbang.or.kr',
    'license': 'GNU Affero General Public License v3 or later (AGPLv3+)',
    #'url': 'https://github.com/mete0r/myapp',

    'packages': [
        'myapp'
    ],
    'package_dir': {'': 'src'},
    'install_requires': [
    ],
    'entry_points': {
        #'console_scripts': ['myapp = myapp.main:main']
    }
}

setup(**setup_info)