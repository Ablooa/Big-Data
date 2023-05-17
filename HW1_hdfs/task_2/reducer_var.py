#!/usr/bin/env python

import sys

m_i = 0
c_i = 0
v_i = 0

for line in sys.stdin:
    c, m, v = map(float, line.strip().split(','))
    
    v_i = (v_i*c_i + v*c)/(c_i + c)+c_i*c*((m_i-m)/(c_i+c))**2
    m_i = (m_i*c_i+m*c)/(c_i+c)
    
    c_i += c

with open('var.txt', 'w') as f:
    f.write(str(v_i))

