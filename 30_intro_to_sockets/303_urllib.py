from urllib.parse import urlparse
import sys

"""
This program demonstrates how to parse a URL using urlib.parse
"""

while True:
    text = sys.stdin.readline().strip()
    if len(text)==0:
        break
    split = urlparse(text);
    print( split )
    print( "scheme:  ", split[0] )   # scheme
    if split[0] == 'http' or split[0] == '':
        print("    that is TCP and HTTP protocol on port 80")
    elif split[0] == 'https':
        print("    that is TCP with SSL wrapper and HTTP protocol on port 443")
    else:
        print("    that is an unsupported protocol")
    print( "host:    ", split[1] )   # hostname
    print( "path:    ", split[2] )   # path to page
    print( "params:  ", split[3] )   #
    print( "query:   ", split[4] )   # query string
    print( "fragment:", split[5] )   #
