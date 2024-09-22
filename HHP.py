# Hello All

import sys
import time

# Globals
OXY_LIST = []
OXY_ZERO = 0



def Pulse(heart_rate: int):
    if isinstance(heart_rate, int):
        if heart_rate < 0: # if heart rate is less than 0
            return "Low"
        if heart_rate < 20 : # if heart rate is less than 20
            return "Highest"
        if heart_rate < 40: # if heart rate is less than 40
            return "Medium"
        if heart_rate <= 130: # if heart rate is less than or equal to 130
            return "Low"
        if heart_rate <= 170: # if heart rate is less than or equal to 170
            return "Medium"
        if heart_rate <= 210: # if heart rate is less than or equal to 210
            return "Highest"
        else:
            return "Impossible"
    else:
        return "Low"


def BloodOxygen(percent):
    global OXY_ZERO
    total = 0
    alarm = 0

    if percent > 99.9 or percent < 0:
        print("Input not possible.")
        return
    # Adds the new reading and gets rid of the oldest one
    if len(OXY_LIST) >= 6:
        OXY_LIST.pop(0)
        OXY_LIST.append(percent)
    else:
        OXY_LIST.append(percent)

    # Used for checking if the oxygen reader fell off the finger
    if percent == 0:
        OXY_ZERO += 1
    else:
        OXY_ZERO = 0
    if OXY_ZERO >= 3:
        i = 0
        for x in range(len(OXY_LIST)):
            if OXY_LIST[x] != 0:
                total += OXY_LIST[x]
            else:
                i += 1
        avg = total / i
        print("equipment fell off finger")
        # return avg


    # Adds up the readinggs and gets the avereage
    for x in range(len(OXY_LIST)):
        total += OXY_LIST[x]
    avg = total / len(OXY_LIST)

    if percent <= 50:
        alarm = 3
    elif percent <= 80:
        alarm = 2
    elif percent <= 85:
        alarm = 1
    return (avg, alarm)

def increment_time(hours, mins, increment=10):
    # Increase minutes by the increment value (default is 10)
    mins += increment
    if mins >= 60:
        mins -= 60
        hours += 1
    if hours >= 24:
        hours = 0  # Reset to 00 after 24 hours
    return hours, mins

def format_time(hours, mins):
    return f"{hours:02d}:{mins:02d}"

def Bloodpressure(input):
    alarm = ''
    values = input.split('/')
    systolic = int(values[0])
    diastolic = int(values[1])
    
    if (systolic > 200 or diastolic > 120) or (systolic < 70 or diastolic > 40):
        alarm = "Blood pressure medium"
    elif systolic > 150 or diastolic > 90:
        alarm = "Blood pressure low"
    elif systolic < 50 or diastolic < 33:
        alarm = "Blood pressure dangerously high" 
    elif systolic > 230 or diastolic > 150:
        alarm = "equiment error"
    else:
        alarm = "Blood pressure normal"
        
    return alarm

    
def main():
    #Open the file with data
    f = open(sys.argv[1],"r")
    hours = 0
    mins = 0

    #Read contents line by line
    for x in f:
        print(x)
        line = x.split()
        #Print line[] Statements for debugging purposes only
        #Code for proccessing Pulse Rate
        line[0]
        pulse = int(line[0])
        #print(line[0])
        #Check if data exists for Blood Preassure
        #If so, proccess it
        current_time = format_time(hours, mins)
        print("Time:", current_time)
        
        # Increment time by 10 minutes
        hours, mins = increment_time(hours, mins)

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
        print("Pulse alarm level: ", Pulse(pulse))

        #Call methods for Blood Oxygen
        avg, BOL = BloodOxygen(bloodoxygen)
        print(f"Blood Oxy avg: {avg:.2f}", "Blood Oxy alarm level: ", BOL)

        #Call methods for Blood Preassure
        print(Bloodpressure(bloodpreassure))
        time.sleep(1)

    #close the file
    f.close()


if __name__ == "__main__":
    main()
