#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :
    return [x, y, z]

assert f(2, 3)       == [2, 3, ()] #packing nothing for z
assert f(2, 3, 4)    == [2, 3, (4,)]
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
assert f(2, 5,  t)  == [2, 5, ((3, 4),)] # doesn't care what the type is or if it is already a tuple, it will still get put in a tuple
assert f(2, 5, *t)  == [2, 5, (3, 4)] # unpack into the parameter, then the function packs the things that were unpacked
assert f(2, *t)     == [2, 3, (4,)] # 3 is assigned to y, 4 is left to be unpacked in the tuple
assert f(*t)        == [3, 4, ()]

u = (2,)
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()] # in either case, unpacking the iterable happens first

d1 = {"y" : 3, "x" : 2}
assert f(**d1) == [2, 3, ()] # "**" is dictionary unpacking, y= 3, x=2, and nothing is packed at the end

d2 = {"y" : 3}
assert f(2,     **d2) == [2, 3, ()]
assert f(x = 2, **d2) == [2, 3, ()] # y = 3

print("Done.")
