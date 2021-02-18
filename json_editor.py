#!/usr/bin/python3

import json

def load_json(file):
    with open(file) as f:
        return json.loads(f.read())

def store_json(file, payload):
    with open(file, 'w') as f:
        json.dump(payload, f, indent = 4)



