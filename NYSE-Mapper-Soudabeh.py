#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# this line means that the script is executable


# import the module for reading and writing data
import sys

# input is read by STDIN (standard input) and do the following for each
# input line
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line by comma separator to produce a list
    line = line.split(",")

    # avoid the column headers
    if line[0] == 'exchange':
        continue
    
    # assign first value of the list to the ticker
    ticker = line[1]

    # assign the third value to the trade price
    tradePrice = line[4]

    # mapper prints ticker and trade price with a tab in between, taken as input by the reducer
    print(f'{ticker}\t{tradePrice}')
   

