import sys
import os

sys.path.append(os.path.abspath("FlaskWebProject"))
from FlaskWebProject import random_string

def test_password():
    assert len(random_string.getNewPassword(10)) == 10
    assert random_string.getNewPassword(-1) == ''
    assert random_string.getNewPassword(10.5) == ''
    assert random_string.getNewPassword("blabla") == ''
    assert random_string.getNewPassword(None) == ''
    assert random_string.getNewPassword(True) == ''
    assert random_string.getNewPassword(300) == ''

