import os
import importlib

env = '.' + os.environ.get('ENVIRONMENT', 'dev')
print("Environment is {env}".format(env=env))
module = importlib.import_module(env, 'poolmaster.settings')

globals().update(vars(module))
