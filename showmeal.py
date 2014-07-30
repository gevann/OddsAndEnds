import json, sys

args = sys.argv
if len( args ) < 2:
    print "Usage:  $python showmeal.py <mealfile num> (option = <b/l/d>)"
    sys.exit()

meal = "";
data_file_path = "/Users/graemenathan/Documents/Exercise/dailymeals/meal" + args[1] +".json"
jdata = open( data_file_path )
data = json.load( jdata )

def show( L, n ):
    out = ""
    tabs = n * "   "
    for x in L:
        if isinstance( L[x], dict ):
            #is a dictionary, recurse
            out += tabs + x + ":\n" + show( L[x], n+1) 
        else:
            out += tabs + x + ": " + L[x] +"\n"
    return out

if( len(args) == 3 ):
    data = data[args[2]]

print( show( data, 0 ) ) 

