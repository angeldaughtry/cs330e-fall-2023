#!/usr/bin/env python3

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3.8/library/exceptions.html

def f (b) :
    if b : #if b is true
        raise NameError("abc")
    return 0 #if b is false

print("Exceptions.py")

try :
    assert f(False) == 0 #put statement we expect to cause trouble bc f(False) returns 0
except NameError : #this gets skipped
    assert False

try :
    assert f(True) == 1 #this doesn't happen bc an expection is raised, everything stops at this point and goes to the expection block
    assert False # does not excecute
except NameError as e : #alias NameError as e
    assert isinstance(e,      NameError)
    assert isinstance(e.args, tuple)
    assert len(e.args)  ==     1
    assert e.args       is not ("abc",)
    assert e.args       ==     ("abc",)
else : # does not execute
    assert False 

assert isinstance(NameError, type)
assert isinstance(type,      type)

assert issubclass(NameError,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(NameError,     BaseException)
assert issubclass(BaseException, object)

print("Done.")
