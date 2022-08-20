# MOCKING SYS ARGUMENT PASS
from os import environ as env
import os
import sys

env['ENV'] = 'local'

if env['ENV'] == 'local':
    env['FEATURE_OUTPUT_LOC'] = '/Users/aniketkamavisdar/IpyNotebooks/featureSet_export/'
    env['APP_DIR'] = env['PWD'] + '/..'
    env['JOB_CONFIGURATIONS'] = env['APP_DIR'] + '/resources/'
    env['PACKAGE_DIR'] = env['JOB_CONFIGURATIONS'] + '/artifacts'
    env['GOOGLE_APPLICATION_CREDENTIALS'] = env['JOB_CONFIGURATIONS'] + "/cred.json"
    sys.path.append(os.path.abspath(env['PACKAGE_DIR']))

from configs import logger
log = logger.logger.get_logger()
log.info("Running local...")

from src import main

main.__main()
