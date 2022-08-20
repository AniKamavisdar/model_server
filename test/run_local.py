# MOCKING SYS ARGUMENT PASS
from os import environ as env
import os
import sys

print("RUNNING TEST SCRIPT....")
env['ENV'] = 'local'

if env['ENV'] == 'local':
    env['FEATURE_OUTPUT_LOC'] = '/Users/aniketkamavisdar/IpyNotebooks/featureSet_export/'
    env['JOB_CONFIGURATIONS'] = env['PWD'] + '/..' + '/resources/'
    env['PACKAGE_DIR'] = env['JOB_CONFIGURATIONS'] + '/artifacts'
    env['GOOGLE_APPLICATION_CREDENTIALS'] = env['JOB_CONFIGURATIONS'] + "/cred.json"
    sys.path.append(os.path.abspath(env['PACKAGE_DIR']))

from src import main

main.__main()
