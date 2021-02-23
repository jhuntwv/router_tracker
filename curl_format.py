#!/usr/bin/python3
from markup_editor import *
import sys

# I had some misunderstandings about how stdin works, i can tell its more like manipulating a file,
# will come back to this later
store_json(sys.argv[1], sys.stdin) 
