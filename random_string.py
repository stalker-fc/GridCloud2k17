import string
import random


def getNewPassword(length):
    if type(length) is not int:
        return ''
    if length < 0:
        return ''

    res = []
    pass_symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&+,-./:;=?@[\]^_"

    random.seed()
    for i in range(length):
        res.append(random.choice(pass_symbols))
    return ''.join(res)
