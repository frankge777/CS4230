import HHP
import pytest

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
    
    
def test_BloodOxygen():
    pass
    
def test_Bloodpressure():
    pass
def test_increment_time():
    assert HHP.increment_time(0,0) == (0,10)
     
def test_format_time():
    assert HHP.format_time(0,0) == "00:00"
    assert HHP.format_time(0,10) == "00:10"
    assert HHP.format_time(23,59) == "23:59"