import HHP
import pytest
import subprocess

def test_pulse():
    assert HHP.Pulse(130) == ("Low", 1)
    assert HHP.Pulse(170) == ("Medium", 2)
    assert HHP.Pulse(210) == ("Highest", 3)
    assert HHP.Pulse(0) == ("Highest", 3)
    assert HHP.Pulse(20) == ("Highest", 3)
    assert HHP.Pulse(40) == ("Medium", 2)
    assert HHP.Pulse(130) == ("Low", 1)
    assert HHP.Pulse(170) == ("Medium", 2)
    assert HHP.Pulse(210) == ("Highest", 3)
    assert HHP.Pulse("210") == ("Low", 1)
    assert HHP.Pulse(260) == ("Impossible", 1)
    
def test_BloodOxygen():
    assert HHP.BloodOxygen(100) == (None)
    assert HHP.BloodOxygen(-1) == (None)
    
def test_Bloodpressure():
    pass
def test_increment_time():
    assert HHP.increment_time(0,0) == (0,10)
     
def test_format_time():
    assert HHP.format_time(0,0) == "00:00"
    assert HHP.format_time(0,10) == "00:10"
    assert HHP.format_time(23,59) == "23:59"
    


def test_main_function():
    # Create a test input file
    with open('test_input.txt', 'w') as f:
        f.write('86 92 120/80\n')
        f.write('88 91.5\n')
        f.write('88 91.3\n')
        f.write('87\n')
        f.write('85 89.4\n')
        f.write('84 89.0 122/81\n')

    # Run the main function and capture its output
    output = subprocess.check_output(['python', 'HHP.py', 'test_input.txt'])
    assert output == b"Time: 00:00\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 92.00 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\nTime: 00:10\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.75 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\nTime: 00:20\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.60 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\nTime: 00:30\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.53 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\nTime: 00:40\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.10 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\nTime: 00:50\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 90.75 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n"
    
    # Assert the expected output
    # You can add assertions here to check the output of the main function

def test_main_function2():
    # Define the input data as chunks (one or two lines at a time)
    input_data_chunks = [
        '86 92 120/80\n',  # Chunk 1: First line
        '88 91.5\n',       # Chunk 2: Second line
        '88 91.3\n',       # Chunk 3: Third line
        '87\n',            # Chunk 4: Fourth line
        '85 89.4\n',       # Chunk 5: Fifth line
        '84 89.0 122/81\n' # Chunk 6: Sixth line
    ]

    expected_output = [
        b"Time: 00:00\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 92.00 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n",
        b"Time: 00:10\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.75 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n",
        b"Time: 00:20\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.60 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n",
        b"Time: 00:30\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.53 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n",
        b"Time: 00:40\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 91.10 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n",
        b"Time: 00:50\r\nPulse alarm level:  ('Low', 1)\r\nBlood Oxy avg: 90.75 Blood Oxy alarm level:  0\r\nBlood pressure medium\r\n"
    ]
    
    for i, chunk in enumerate(input_data_chunks):
        # Write the current chunk to the input file
        with open('test_input.txt', 'w') as f:
            f.write(chunk)

        # Run the program with the current chunk
        output = subprocess.check_output(['python', 'HHP.py', 'test_input.txt'])

        # Verify that the output matches the expected output for this chunk
        assert output == expected_output[i]


