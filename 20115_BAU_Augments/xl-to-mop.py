import os
import sys

filename = sys.argv[1]
cmd1 = 'python augment.py ' + filename
cmd2 = 'ansible-playbook -i router_names.yml generate_router_config.yml'
cmd3 = 'rm generate_router_config.retry'
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
