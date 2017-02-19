from __future__ import print_function
import os
import urllib
import fbchat

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()

parser.read('/home/pi/Documents/GitHub/grades/config.ini')

pdfLink = "http://csiflabs.cs.ucdavis.edu/~ssdavis/60/60w17.pdf"
pdfLoc = "/home/pi/Documents/GitHub/grades/60w17.pdf"
output = "/home/pi/Documents/GitHub/grades/out.txt"
#gets PDF from website and converts to ASCII
def getPdf():
    testfile = urllib.URLopener()
    testfile.retrieve(pdfLink, pdfLoc)

    os.system(("ps2ascii %s %s") %(pdfLoc, output))

#gets the timestamp of PDF
def checkTime():
    f = open(output)
    allGrades = f.read()
    firstLine = allGrades.split('M', 1)[0] #stops at the end of the line, either PM or AM
    print(firstLine)
    return firstLine

#finds my ID, prints my grades
def myGrade():
    myID = parser.get('myID', 'number')
    f = open(output)
    message = ''
    for line in f:
        char = 0
        found = 0 
        while(char != 5000):
            if(line[char:char+4] == myID): #finds my ID
                found = 1;
                break
            char=char+1
        
        if(found == 1):
            while(line[char].isalpha() == False): #prints all characters until it hits a letter (my grade)
                if(line[char] == ' '):
                    message = message + ' | '
                else:    
                    print(line[char], end='')
                    message = message + line[char]
                char=char+1
                
            #prints grade    
            if(line[char+1] == '+' or line[char+1] == '-'):
                print(line[char] + line[char+1])
                message = message + line[char] + line[char+1]

            else:
                print(line[char])
                message = message + line[char]
            
    return(message)


def fbMessege(message):
    username = parser.get('messenger', 'myUsername')
    password = parser.get('messenger', 'myPassword')
    UID = parser.get('messenger', 'myUID')

    client = fbchat.Client(username, password)

    sent = client.send(UID, message)

    if sent:
        print("Message sent successfully!")
                
def main():

    cts = checkTime() #gets current download timestamp

    getPdf() #downloads pdf from URL

    nts = checkTime() #gets new download timestamp

    if(cts != nts):  #if new pdf is updated, print my grade
        message = "New grade! Here's the info:\n" + myGrade() + "\nClick here for more details: " + pdfLink
        fbMessege(message)
    
main()
