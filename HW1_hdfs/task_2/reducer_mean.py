#!/usr/bin/env python

import sys

m_i = 0
c_i = 0

for line in sys.stdin:
    c, m, v = map(float, line.strip().split(','))
    
    m_i = (m_i*c_i+m*c)/(c_i+c)
    c_i += c

with open('mean.txt', 'w') as f:
    f.write(str(m_i))

