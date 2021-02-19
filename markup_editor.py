#!/usr/bin/python3

import json
import xmltodict
import yaml

def load_json(file):
    with open(file) as f:
        return json.loads(f.read())

def store_json(file, payload):
    with open(file, 'w') as f:
        json.dump(payload, f, indent = 4)

def load_xml(file):
    with open(file) as f:
        return xmltodict.parse(f.read())

def store_xml(file, payload):
    with open(file, 'w') as f:
        f.write(xmltodict.unparse(payload, pretty=True))

def load_yaml(file):
    with open(file) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)

def store_yaml(file, payload):
    with open (file, 'w') as f:
        f.write(yaml.dump(payload, default_flow_style=False))
