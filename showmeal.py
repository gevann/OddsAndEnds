import json
import sys

args = sys.argv
if len( args ) < 2:
    print "usage:  $python showmeal.py <mealfile.txt> (option = <b/l/d>)"

meal = "";
jdata = open( args[1] )
data = json.load( jdata )

def show( L, n ):
    out = ""
    tabs = n * "   "
    for x in L:
        if isinstance( L[x], dict ):
            #is a dictionary, recurse
            out += tabs + x + ":\n" + show( L[x], n+1) 
           # show(L[x], n+1 ) 
        else:
            out += tabs + x + ": " + L[x] +"\n"
    return out

if( len(args) == 3 ):
    data = data[args[2]]

print( show( data, 0 ) ) 

