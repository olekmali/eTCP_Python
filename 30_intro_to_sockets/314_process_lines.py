import sys

"""
This program demonstrates how to read data line by line until an empty line is received
"""

while 1:
    data = sys.stdin.readline().strip()
    if len(data)==0:
        break
    else:
        print len(data)
