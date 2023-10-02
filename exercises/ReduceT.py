#!/usr/bin/env python3

# ----------
# ReduceT.py
# ----------

# https://docs.python.org/3/library/functools.html

from functools import reduce
from operator  import add, sub
from unittest  import main, TestCase

from Reduce import    \ # the functions that you implement from your file
    reduce_for_range, \
    reduce_for,       \
    reduce_while

class MyUnitTests (TestCase) : #class derived from test case
    def setUp (self) : # run every time you set up the unit test
        self.a = [ # alias them in a list and iterate through instead of writing a test for each one
            reduce_for_range,
            reduce_for,
            reduce_while,
            reduce]

    def test_1 (self) : # one unit test
        for f in self.a : #iterate through the functions
            with self.subTest() : #keep going if failure
                self.assertEqual(f(None, [],       0),  0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2],       1),  3) # start at 1, add 2 = 3

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2, 3, 4], 0),  9) # start at 0 add 2, 2+3 = 5, 5+4 = 9

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 0), -9)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% ReduceT
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
"""
