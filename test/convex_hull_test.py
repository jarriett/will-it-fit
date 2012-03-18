from wif_lib.convex_hull import *
from wif_lib.geometry import *
from math import pi

def test_calc_determinate_right():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,2))

  d = calc_determinant(p)

  print 'determinant :  %s' % (repr(d))
  
  assert d < 0 

def test_calc_determinate_neutral():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,3))
  
  d = calc_determinant(p)

  print 'determinant :  %s' % (repr(d))
  
  assert(d == 0)

def test_calc_determinate_left():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,4))

  d = calc_determinant(p)

  print 'determinant :  %s' % (repr(d))

  assert(d>0)

def test_is_right_turn_neutral_is_false():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,3))

  flag = is_right_turn(p)

  print 'flag :  %s' % (flag)
  
  assert(not flag)

def test_is_right_turn_is_true():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,2))

  flag = is_right_turn(p)

  print 'flag :  %s' % (flag)

  assert(flag)

def test_is_right_turn_is_false():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(3,4))

  flag = is_right_turn(p)

  print 'flag :  %s' % (flag)

  assert(not flag)

def test_remove_duplicates():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(2,2))
  p.append(Point(3,3))
  p.append(Point(3,3))

  fixed = remove_duplicates(p)

  for pt in fixed:
    print pt

def test_generate_convex_hull():

  p = []
  p.append(Point(1,1))
  p.append(Point(2,2))
  p.append(Point(1,3))
  p.append(Point(3,3))
  p.append(Point(3,1))

  result = generate_convex_hull(p)
  print 'RESULT:'
  for pt in result:
    print pt
