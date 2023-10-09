#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4) # defining a tuple
assert t            == (3, 4) #check if it is correct
assert t            != (4, 3) # order matters in tuples
assert f(2, t, 5)   == [2, (3, 4), 5] # calling the function, passes the arguements, returns the list with those values
assert f(2, 5, t)   == [2, 5, (3, 4)] # same as previous
assert f(2, *t)     == [2, 3, 4] # "*" means unpacking
assert f(z = 2, *t) == [3, 4, 2] # 
assert f(*t, z = 2) == [3, 4, 2]

# f(*t)        # TypeError: f() missing 1 required positional argument: 'z' (only 2 in the iterable unpacking)
# f(2, 3, *t)  # TypeError: f() takes 3 positional arguments but 4 were given (too many arguments)
# f(x = 2, *t) # TypeError: f() got multiple values for argument 'x' (by name --> iterable unpacking is in the wrong order, will try to reassign x - x is orginally 3 from the unpacking but then trys to become 2 for by variable name, see notes)


d = {"z" : 4, "y" : 3, "x" : 2} # unpacking drops the curly braces and see the colons as "=" (the key must be corresponding)
assert f(**d) == [2, 3, 4]

# f(2,     **d) # TypeError: f() got multiple values for argument 'x'
# f(x = 2, **d) # TypeError: f() got multiple values for keyword argument 'x'

d = {"z" : 4, "y" : 3}
assert f(2, **d) == [2, 3, 4] # unpack the dictionary, y and z are now passed by variable name

# f(**d, 2) # SyntaxError: invalid syntax

assert f(x = 2, **d) == [2, 3, 4] # no problem with flipping by name and dictionary unpacking
assert f(**d, x = 2) == [2, 3, 4]

d = {"y" : 3}
assert f(2, z = 4, **d) == [2, 3, 4]
assert f(2, **d, z = 4) == [2, 3, 4]

t = (3,)
d = {"z" : 4}
assert f(2,     *t, **d) == [2, 3, 4]
assert f(y = 3, *t, **d) == [3, 3, 4]
assert f(*t, y = 3, **d) == [3, 3, 4]
assert f(*t, **d, y = 3) == [3, 3, 4]

# assert f(x = 2, *t, **d) == [2, 3, 4] # TypeError: f() got multiple values for argument 'x' (x is being assigned twice)

print("Done.")
