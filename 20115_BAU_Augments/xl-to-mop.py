import os
import sys

filename = sys.argv[1]
cmd1 = 'python augment.py ' + filename
cmd2 = 'ansible-playbook -i router_names.yml generate_router_config.yml'
os.system(cmd1)
os.system(cmd2)

