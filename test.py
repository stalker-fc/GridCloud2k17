import sys
import os

sys.path.append(os.path.abspath("FlaskWebProject"))
from FlaskWebProject.random_string import getNewPassword

def test_password():
    assert len(getNewPassword(10)) == 10
    assert getNewPassword(-1) == ''
    assert getNewPassword(10.5) == ''
    assert getNewPassword("blabla") == ''
    assert getNewPassword(None) == ''
    assert getNewPassword(True) == ''
    assert getNewPassword(300) == ''

