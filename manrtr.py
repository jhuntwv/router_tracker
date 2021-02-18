#!/usr/bin/python3

import csv
import sys

LIST = sys.argv[2]
ROUTER_FIELDS = ['hostname','ip address','location']

def read_router():
    with open(LIST,'r') as f:
        for i in csv.reader(f):
            print(f'{i[0]} is in {i[2]} and has IP {i[1]}')

def add_router():
    with open(LIST,'a') as f:
        csv.writer(f).writerow([input(f'{ROUTER_FIELDS[i]}: ') for i in range(0,3)])
    read_router()

{'display': read_router, 'add': add_router}[sys.argv[1]]()  #start the appropriate function




