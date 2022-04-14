import sys

"""
This program demonstrates conversion from text to array of bytes and back to text
"""

while True:
    instr = str( sys.stdin.readline() )
    if len(instr.strip())==0:
        break
    data = bytes( instr, 'UTF-8')
    print( "data: >>", data, "<<" )
    text = str( data, 'UTF-8' )
    print( "text: >>", text, "<<"  )
    text = text.strip()
    print( "strp: >>", text, "<<"  )
