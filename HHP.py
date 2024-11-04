# Hello All

import sys
import time
import os

# Globals
OXY_LIST = []
OXY_ZERO = 0



def Pulse(heart_rate: int):
    try:
        heart_rate = int(heart_rate)
    except ValueError:
        return ("Impossible", "Heart rate monitor malfunction")
    
    alarm = "Low"
    message = "Everything is normal"

    if heart_rate < 0: # if heart rate is less than 0
            alarm = "Low"
            message = "Heart rate must be positive"
            
    elif heart_rate <= 20 : # if heart rate is less than or equal to 20
            alarm = "Highest"
            message = "Heart rate dangerously low"
            
    elif heart_rate <= 40: # if heart rate is less than  or equal to 40
            alarm = "Med"
            message = "Heart rate low" 
            
    elif heart_rate <= 130: # if heart rate is less than or equal to 130
            alarm = "None"
            message = "Everything is normal"
            
    elif heart_rate <= 170: # if heart rate is less than or equal to 170
            alarm = "Med"
            message = "Heart rate elevated"
            
    elif heart_rate <= 210: # if heart rate is less than or equal to 210
            alarm = "Highest"
            message = "Heart rate dangerously high"
            
    else:
            alarm = "Impossible"
            message = "Heart rate monitor malfunction"

    return (alarm, message)


def BloodOxygen(percent):
    global OXY_ZERO
    total = 0
    alarm = 0
    badInput = False
    message = "Everything is normal"

    if percent > 99.9 or percent < 0:
        badInput = True
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
        message = "* Check device connection *"
        return ("Low", message)
        # return avg

    # Adds up the readinggs and gets the avereage
    for x in range(len(OXY_LIST)):
        total += OXY_LIST[x]
    avg = total / len(OXY_LIST)

    if avg > 85:
        alarm = "None"
        # return("None", message)
    elif avg <= 50:
        alarm = "High"
        message = "Blood Oxygen level dangerously Low"
    elif avg <= 80:
        alarm = "Med"
        message = "Blood Oxygen level Low"
    elif avg <= 85:
        alarm = "Low"
        message = "Blood Oxygen level Low"
    if badInput == True:
        return ("Low", "Input not possible")
    
    return (alarm, message) 


def increment_time(hours, mins, increment=10):
    # Increase minutes by the increment value (default is 10)
    mins += increment
    if mins >= 60:
        mins -= 60 # would this just reset to 0?
        hours += 1
    if hours >= 24:
        hours = 0  # Reset to 00 after 24 hours
    return hours, mins

def format_time(hours, mins):
    return f"{hours:02d}:{mins:02d}"

def Bloodpressure(input):
    alarm = ''
    level = ''
    values = input.split('/')
    systolic = int(values[0])
    diastolic = int(values[1])
    
    if (systolic > 200 or diastolic > 120) or (systolic < 70 or diastolic > 40):
        level = 'Med'
        alarm = "Blood pressure medium"
    elif systolic > 150 or diastolic > 90:
        level = 'low'
        alarm = "Blood pressure low"
    elif systolic < 50 or diastolic < 33:
        level = 'high'
        alarm = "Blood pressure dangerously high" 
    elif systolic > 230 or diastolic > 150:
        level = 'Med'
        alarm = "equiment error"
    else:
        level = 'normal'
        alarm = "Blood pressure normal"
        
    return (level,alarm)

def is_text_file(filename):
    return filename.endswith(('.txt', '.dat')) 

def print_func(alarm, message):
    print(f"\t{alarm} - {message}") # print("alarm, message)


def process_data(lines):
    hours = 0
    mins = 0
    for line in lines:
        bloodpressure = None
        bloodoxygen = None
        line = line.strip().split()
        if line:
            pulse = line[0]
            current_time = format_time(hours, mins)
            print("Time:", current_time)
            hours, mins = increment_time(hours, mins)  # increment time by 10 seconds

            if len(line) > 1:
                if "/" in line[1]:
                    bloodpressure = line[1]
                else:
                    bloodoxygen = float(line[1])

            if len(line) > 2:
                bloodpressure = line[2]

            # Process Pulse
            pulse_alarm, pulse_message = Pulse(pulse)
            print_func(pulse_alarm, pulse_message)

            # Process Blood Oxygen if present
            if bloodoxygen is not None:
                avg, BOL = BloodOxygen(bloodoxygen)
                print_func(avg, BOL)

            # Process Blood Pressure if present
            if bloodpressure is not None:
                bloodpressure_alarm, bloodlevel = Bloodpressure(bloodpressure)
                print_func(bloodpressure_alarm, bloodlevel)
            else:
                print_func("None", "No reading was received")
            print("\n")
            time.sleep(1)

def main():
    input_bool = True
    while input_bool:
        input_file = input("Enter name of input file (or type 'input' to enter data manually): ")

        if input_file.lower() == 'input':
            print("Please enter your data line by line. Type 'done' when you are finished.")
            lines = []
            while True:
                user_input = input()
                if user_input.lower() == 'done':
                    break
                lines.append(user_input)
            process_data(lines)
            input_bool = False
        elif os.path.isfile(input_file):
            with open(input_file) as f:
                lines = f.readlines()
            process_data(lines)
            input_bool = False
        else:
            print("File not found. Please provide a valid file or enter data manually.")

if __name__ == "__main__":
    main()

