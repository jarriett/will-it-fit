from math import sin,sqrt,atan

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
      return "x: %s , y: %s" % (self.x,self.y)

    def __eq__(self,other):
      return (self.x == other.x and self.y == other.y)

    def get_tuple(self):
      return (self.x,self.y)

class Line:
    def __init__(self,start,finish):
      self.start = start
      self.finish = finish

    def __str__(self):
      return "start: %s , finish: %s" % (self.start,self.finish)


def rotate_a_shape(lines,rotation,pivot):
    r_lines = []

    for line in lines:
      start = rotate_a_point(line.start,rotation,pivot)
      end = rotate_a_point(line.finish,rotation,pivot)
      r_lines.append(Line(start,end))

    return r_lines

def rotate_a_point(point, rotation, pivot):
    total_rotation = current_angle_in_rad(point,pivot) + rotation
    radius = calculate_radius_from_center(point,pivot)

    new_y = calc_y_component_from_angle_and_radius(radius,total_rotation)  
    new_x = x_component_from_y(pivot,new_y,radius)
    
    return Point(new_x,new_y)
        
def current_angle_in_rad(p,c):
    adj = p.x -c.x
    opp = p.y -c.y
    
    if(opp == 0 or adj ==0):
        return atan(0)
   
    return atan(opp/adj)    

def calculate_radius_from_center(p,c):
    return sqrt(pow(p.x - c.x,2) + pow(p.y- c.y,2))

def x_component_from_y(center_point, y, radius):
    try:
      return sqrt(pow(radius,2) - pow((y-center_point.y),2)) + center_point.x
    except ValueError:
      print "center_point: %s, y: %s, radius: %s" % (center_point, y , radius)
      print "pow-radius:(pow(radius,2))  %s" % (pow(radius,2))
      print "pow-center:(pow((y-center_point.y),2)) %s" % (pow((y-center_point.y),2))
      raise

def calc_y_component_from_angle_and_radius(radius, angle):
    return sin(angle) * radius

def get_center_of_canvas(x,y):
    x = x/2
    y = y/2
    return Point(x,y)

def create_enclosed_shape_from_points(pts):
    lines = [] 

    for counter,pt in enumerate(pts):
      lines.append(Line(pt,pts[counter+1]))
      if counter == len(pts) -2:
        break
    
    lines.append(Line(pts[len(pts)-1],pts[0]))
      
    return lines 
