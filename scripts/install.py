#!/usr/bin/env /usr/bin/python
# Review this with a pair bc you don't understand half of it :)

import os
from subprocess import call

PYTHON_VERSION = '3.6.2'
VIRTUALENV_NAME = 'to_the_polls'
SHELL = os.environ['SHELL']
CALL_FAILED = False


def run(expression):
    global CALL_FAILED
    if not CALL_FAILED:
        call_result = call(expression, shell=True, executable=SHELL)
        if call_result != 0:
            print(expression + ' failed')
            CALL_FAILED = True


# Install python and create virtualenv
run('pyenv install {}'.format(PYTHON_VERSION))

# rehash shims
run('pyenv rehash')

# Create virtualenv
run('pyenv virtualenv {} {}'.format(PYTHON_VERSION, VIRTUALENV_NAME))

# Activate virtualenv
run('pyenv local {}'.format(VIRTUALENV_NAME))

# Install dependencies
run('pip install -r requirements.txt')
