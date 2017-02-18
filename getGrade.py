import os
import urllib

def getPdf():
    testfile = urllib.URLopener()
    testfile.retrieve("http://csiflabs.cs.ucdavis.edu/~ssdavis/60/60w17.pdf", "60w17.pdf")
    
    output="/home/pi/Documents/GitHub/grades/out.txt"
    os.system(("ps2ascii %s %s") %( '60w17.pdf', output))

def checkTime():
    f = open('out.txt')
    allGrades = f.read()
    firstLine = allGrades.split('PM', 1)[0]
    print(firstLine)
    return firstLine

def myGrade():
    f = open('out.txt')
    

    for i in f:
        z = 0
        found = 0
        while(z != 5000):
            if(i[z:z+4] == '3794'):
                found = 1;
                break
            z=z+1
        
        if(found == 1):
            while(i[z].isalpha() == False):
                print(i[z])
                z=z+1
            
            print(i[z] + i[z+1])
            break

            

            
        
    

def main():
    cts = checkTime()

    getPdf()

    nts = checkTime()

    if(cts == nts):
        myGrade()

    
main()
