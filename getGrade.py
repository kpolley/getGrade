import os
import urllib

def main():

    testfile = urllib.URLopener()
    testfile.retrieve("http://csiflabs.cs.ucdavis.edu/~ssdavis/60/60w17.pdf", "60w17.pdf")
    
    output="/home/pi/Documents/GitHub/grades/out.txt"
    os.system(("ps2ascii %s %s") %( '60w17.pdf', output))

    
    
    if '' in open('example.txt').read():
            print "true"

main()