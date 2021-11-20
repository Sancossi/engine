import json
import os


CONFIG_LOCATION = 'data/config'

config = {}

for file in os.listdir(CONFIG_LOCATION):
    with open(os.path.join(CONFIG_LOCATION, file), 'r') as f:
        config[file.split('.')[0]] = json.load(f)
