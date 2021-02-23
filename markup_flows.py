#!/usr/bin/python3

import sys
from markup_editor import *

def format_json_file():
    store_json(sys.argv[1], load_json(sys.argv[1]))

format_json_file()
