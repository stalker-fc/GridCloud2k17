import sys
import os

sys.path.append(os.path.abspath("FlaskWebProject"))
from FlaskWebProject.random_string import getNewPassword

def test_password():
    assert len(getNewPassword(10)) == 10
    assert len(getNewPassword(-1)) == 0
    assert len(getNewPassword(10.5)) == 0
    assert len(getNewPassword("blabla")) == 0
    assert len(getNewPassword(None)) == 0
    assert len(getNewPassword(True)) == 0

