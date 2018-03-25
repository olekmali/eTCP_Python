import sys

"""
This program demonstrates how to read data line by line until an empty line is received
"""

while True:
    text = sys.stdin.readline().strip()
    if len(text)==0:
        break
    else:
        print len(text)
