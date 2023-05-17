#!/usr/bin/env python

import sys

for line in sys.stdin:
    if line.startswith('id'):
        continue
    fields = line.strip().split(',')
    if len(fields) < 6:
        continue
    price = float(fields[-7])

    print(f'1,{price},0')
