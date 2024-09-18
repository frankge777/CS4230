import sys
import time

def main():
    #Open the file with data
    f = open(sys.argv[1],"r")

    #Read contents line by line
    for x in f:
        print (x)
        line = x.split()

        #Print line[] Statements for debugging purposes only
        #Code for proccessing Pulse Rate
        line[0]
        pulse = int(line[0])
        #print(line[0])
        #Check if data exists for Blood Preassure
        #If so, proccess it
        if(len(line) > 1):
            if "/" in line[1]:
                bloodpreassure = line[1] 
            else:
                bloodoxygen = float(line[1])
            #print(line[1])
        #Check if data exists for Blood Oxygen Level
        #If so, proccess it
        if(len(line) > 2):
            bloodpreassure = line[2]
            #print(line[2])
        #Wait 10 seconds for the next line to be proccessed

        #Call methods for Pulse

        #Call methods for Blood Oxygen

        #Call methods for Blood Preassure

        time.sleep(1)

    #close the file
    f.close()

print(__name__)
if __name__ == "__main__":
    main()
