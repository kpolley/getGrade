from __future__ import print_function
import os
import urllib

#gets PDF from website and converts to ASCII
def getPdf():
    testfile = urllib.URLopener()
    testfile.retrieve("http://csiflabs.cs.ucdavis.edu/~ssdavis/60/60w17.pdf", "60w17.pdf")
    
    output="/home/pi/Documents/GitHub/grades/out.txt"
    os.system(("ps2ascii %s %s") %( '60w17.pdf', output))

#gets the timestamp of PDF
def checkTime():
    f = open('out.txt')
    allGrades = f.read()
    firstLine = allGrades.split('PM', 1)[0]
    print(firstLine)
    return firstLine

#finds my ID, prints my grades
def myGrade():
    f = open('out.txt')

    
    for line in f:
        char = 0
        found = 0 
        while(char != 5000):
            if(line[char:char+4] == '3794'): #finds my ID
                found = 1;
                break
            char=char+1
        
        if(found == 1):
            while(line[char].isalpha() == False): #prints all characters until it hits a letter (my grade)
                print(line[char], end='')
                char=char+1
                
            #prints grade    
            if(line[char+1] == '+' or line[char+1] == '-'):
                print(line[char] + line[char+1])

            else:
                print(line[char])

def main():
    cts = checkTime() #gets current download timestamp

    getPdf() #downloads pdf from URL

    nts = checkTime() #gets new download timestamp

    if(cts == nts):  #if new pdf is updated, print my grade
        myGrade()

    
main()
