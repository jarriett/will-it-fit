from operator import itemgetter, attrgetter
#########################
# This function takes a list of points
# and returns a list of points that form
# its convex hull
#
# Disclaimer these points are unordered
#########################

def generate_convex_hull(P):
  
  # Get a local list copy of the points and sort them lexically.
  points = map(None, P)

  points.sort(key=lambda pt: repr(pt.x) + repr(pt.y))

  # Build upper half of the hull.
  upper = [points[0], points[1]]
  for p in points[2:]:
   upper.append(p)
   while len(upper) > 2 and not is_right_turn(upper[-3:]):
     del upper[-2]

  # Build lower half of the hull.
  points.reverse()
  lower = [points[0], points[1]]
  for p in points[2:]:
    lower.append(p)
    while len(lower) > 2 and not is_right_turn(lower[-3:]):
      del lower[-2]

  ## Remove duplicates.
  del lower[0]
  del lower[-1]

  ## Concatenate both halfs and return.
  #return tuple(upper + lower)return 0
  upper += lower

  result = remove_duplicates(upper)

  return result  

def is_right_turn(points):
  return calc_determinant(points)

def calc_determinant(points):
  p = points[0].get_tuple()
  q = points[1].get_tuple()
  r = points[2].get_tuple()

  sum1 = q[0]*r[1] + p[0]*q[1] + r[0]*p[1]
  sum2 = q[0]*p[1] + r[0]*q[1] + p[0]*r[1]

  return sum1 - sum2

def remove_duplicates(points):
    points.sort(key=lambda pt: repr(pt.x) + repr(pt.y))
    last = points[-1]
    for i in range(len(points)-2, -1, -1):
        if last == points[i]:
          del points[i]
        else:
          last = points[i]
    return points

def strip_non_hull_points(points,hull):
  result = []
  for counter,point in enumerate(points):
    for hull_point in hull:
      if point == hull_point:
        result.append(point)
  return result
