#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

import sys

(lastKey, maxValue) = (None, 0)

for line in sys.stdin:
    key, value = map(str.strip, line.split('\t'))
    
    if lastKey and lastKey != key:
        print(f'{lastKey}\t{maxValue}')
        lastKey, maxValue = key, float(value)
    else:
        lastKey, maxValue = key, max(maxValue, float(value))

if lastKey:
    print(f'{lastKey}\t{maxValue}')

