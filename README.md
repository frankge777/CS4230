# The Happy Heart Program

## Overview
The Happy Heart Program is designed to monitor the heart functions of a hospital patient. Its main purpose is to raise alarms if there is something seriously wrong and the patient might be at risk. It monitors the following parameters:
- Pulse rate
- Blood pressure
- Blood oxygen level

## Functionality
This program simulates monitoring by reading data either from a file or from the keyboard. Data is read every 10 seconds, with the following specifics:
- Pulse readings are taken every 10 seconds.
- Oxygen levels are normally read every 10 seconds but can occasionally be missing.
- Blood pressure readings are taken at irregular intervals.

The program prints a status update every 10 seconds, including:
- A timestamp
- An alert level (None, Low, Medium, Highest)
- A description of the problem causing the alert
- The associated data

## Input Format
Each input line represents a set of data with:
- A pulse reading
- An oxygen level (which might not be there)
- A blood pressure reading (which is often not there)

Example input:
```
86 92 120/80
88 91.5
88 91.3
87
85 89.4
84 89.0 122/81
```

## Data Characteristics
- **Pulse:** Integer from 0 to 260
- **Oxygen Level:** Percentage from 0 to 99.9 with one decimal place of precision
- **Blood Pressure:** Two integers representing systolic and diastolic readings, usually formatted as `systolic/diastolic`

## Monitoring and Alarms
The program continuously monitors the data and raises alarms to alert nurses of any problems. There are three levels of alarms:
- **Highest:** Life-threatening problem detected
- **Medium:** Dangerous condition detected
- **Low:** Potential problem; maybe an equipment problem

When reporting, only the highest level of alarm is reported. The order of precedence for simultaneous alarms is Pulse, Oxygen, Blood Pressure.

### Alarm Levels
- **Pulse:**
  - Under 20: Highest
  - Under 40: Medium
  - Above 110: Low
  - Above 130: Medium
  - Above 170: Highest
  - Above 210: Impossible

- **Oxygen:**
  - Average below 50%: Highest
  - Average below 80%: Medium
  - Average below 85%: Low
  - Missing for 30 seconds: Low
  - Levels of 0% or less and 100% or higher: Impossible

- **Blood Pressure:**
  - Above 200/120: Medium
  - Above 150/90: Low
  - Below 70/40: Medium
  - Below 50/33: Highest
  - Levels above 230/150: Impossible

## Error Handling
Bad data, including impossible values, are considered equipment malfunctions and reported as minor alarms. The program keeps running despite invalid input, which is reported and not used for monitoring.

## Example Output
```
00:00  Med Alarm  Blood pressure elevated (145/100)
00:10  None       Everything normal
```
Times are in `mm:ss` format and wrap around every hour.

This README provides a basic overview of the Happy Heart Program's functionality, input format, monitoring, and alarm levels. For detailed implementation, refer to the project documentation and code comments.
