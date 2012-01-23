#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    "In: a,b,c = side length. Returns the type of triangle as string."
    sides = sorted([a, b, c])
    if sides[0] <= 0 or sum(sides[0:2]) <= sides[2]:
      raise TriangleError()

    result = "isosceles"
    if len(set([a, b, c])) == 1:
      result = "equilateral"
    elif len(set([a, b, c])) == 3:
      result = "scalene"
    return result

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
