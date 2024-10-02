# Hello All

import sys
import time

# Globals
OXY_LIST = []
OXY_ZERO = 0



def Pulse(heart_rate: int):
    if isinstance(heart_rate, int):
        '''
        Impossible = 1
        Low = 1
        Medium = 2
        Highest = 3'''
        if heart_rate < 0: # if heart rate is less than 0
            return ("Low", 1)
        if heart_rate <= 20 : # if heart rate is less than or equal to 20
            return ("Highest", 3)
        if heart_rate <= 40: # if heart rate is less than  or equal to 40
            return ("Medium", 2)
        if heart_rate <= 130: # if heart rate is less than or equal to 130
            return ("Low", 1)
        if heart_rate <= 170: # if heart rate is less than or equal to 170
            return ("Medium", 2)
        if heart_rate <= 210: # if heart rate is less than or equal to 210
            return ("Highest", 3)
        else:
            return ("Impossible", 1)
    else:
        return ("Low", 1)


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

    if percent <= 50: # less than or equal too 50
        alarm = 3
    elif percent <= 80: # less than or equal too 80
        alarm = 2
    elif percent <= 85: # less than or equal too 85
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
    level = 0
    values = input.split('/')
    systolic = int(values[0])
    diastolic = int(values[1])
    
    if (systolic > 200 or diastolic > 120) or (systolic < 70 or diastolic > 40):
        level = 2
        alarm = "Blood pressure medium"
    elif systolic > 150 or diastolic > 90:
        level = 1
        alarm = "Blood pressure low"
    elif systolic < 50 or diastolic < 33:
        level = 3
        alarm = "Blood pressure dangerously high" 
    elif systolic > 230 or diastolic > 150:
        level = 2
        alarm = "equiment error"
    else:
        level = 0
        alarm = "Blood pressure normal"
        
    return (alarm,level)

    
def main():
    if len(sys.argv) > 1:  # Check if a file is provided in the command line arguments
        input_source = open(sys.argv[1], "r")
    else:
        print("No file specified, switching to interactive mode.")
        input_source = sys.stdin  # Read input from the command line

    hours = 0
    mins = 0

    print("Enter data in the following format: pulse_rate [blood_oxygen] [blood_pressure]\n"
          "For example: 86 92 120/80\n"
          "Type 'exit' to stop input.")

    # Read input line by line
    for x in input_source:
        if x.strip().lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        
        line = x.split()

        if len(line) == 0:
            continue  # Skip empty lines

        pulse = int(line[0])
        bloodoxygen = None
        bloodpressure = None

        current_time = format_time(hours, mins)
        print("Time:", current_time)

        # Increment time by 10 minutes
        hours, mins = increment_time(hours, mins)

        # Process blood oxygen if available
        if len(line) > 1:
            if "/" in line[1]:
                bloodpressure = line[1]
            else:
                bloodoxygen = float(line[1])

        # Process blood pressure if available
        if len(line) > 2:
            bloodpressure = line[2]

        # Output results and alarms
        print("Pulse alarm level: ", Pulse(pulse))

        if bloodoxygen is not None:
            avg, BOL = BloodOxygen(bloodoxygen)
            print(f"Blood Oxy avg: {avg:.2f}", "Blood Oxy alarm level: ", BOL)

        if bloodpressure is not None:
            bloodpressure_alarm, bloodlevel = Bloodpressure(bloodpressure)
            print(bloodpressure_alarm)

    # Close the file if reading from a file
    if input_source is not sys.stdin:
        input_source.close()

if __name__ == "__main__":
    main()
