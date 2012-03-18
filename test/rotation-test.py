from wif_lib.geometry import *
from math import pi

def test_at_90_degree_angle_should_be_radius():
    y = calc_y_component_from_angle_and_radius(2.0,pi/2.0)
    print 'y: %s' % (repr(y))
    assert (y==2.0) 

def test_at_30_degree_angle_should_be_half_radius():
    y = calc_y_component_from_angle_and_radius(2.0,pi/6.0)
    val = sin(pi/6.0) * 2.0
    print 'y: %s' % (repr(y))
    assert (y == val) 

def test_x_from_y():
    c = Point(0,0)
    x = x_component_from_y(c,1,2)
    print 'x: %s' % (repr(x))

def test_x_from_y_where_y_equals_radius():
    c = Point(0,0)
    x = x_component_from_y(c,2,2)
    print 'x: %s' % (repr(x))

def test_calc_center_point_of_canvas():
    c = get_center_of_canvas(640,480)
    assert c.x == 320
    assert c.y == 240

def test_calculate_radius_from_center():
    r = calculate_radius_from_center(Point(0,0),Point(1,1))
    print 'r: %s' % (repr(r))

def test_calculate_points_angle_from_center():
    a = current_angle_in_rad(Point(0,0),Point(1,1))
    print 'a: %s' % (repr(a))

def test_calculate_points_angle_from_center_for_zero():
    a = current_angle_in_rad(Point(0,0),Point(0,0))
    print 'a: %s' % (repr(a))

def test_rotate_a_point():
    c = Point(0,0)
    p = Point(1,1) 

    rot = rotate_a_point(p,.785,c)
    
    print 'rot %s:%s' % (rot.x,rot.y)
    

def test_create_enclosed_shape_from_points():
    #input - 3 points  - (0,0), (2,0) , (1,1)
    #output - 3 lines  - 
    #     1.  (0,0) -> (2,0)
    #     2.  (2,0) -> (1,1)
    #     3.  (1,1) -> (0,0)
    ins = [Point(0,0),Point(2,0),Point(1,1)]
    out = create_enclosed_shape_from_points(ins)
    
    #line 1
    line1 = out[0]
    assert(line1.start.x == 0)
    assert(line1.start.y == 0)
    assert(line1.finish.x == 2)
    assert(line1.finish.y == 0)
    
    line2 = out[1]
    assert(line2.start.x == 2)
    assert(line2.start.y == 0)
    assert(line2.finish.x == 1)
    assert(line2.finish.y == 1)

    line3 = out[2]
    assert(line3.start.x == 1)
    assert(line3.start.y == 1)
    assert(line3.finish.x == 0)
    assert(line3.finish.y == 0)

def test_rotate_a_point_640480_canvas():
    c = Point(320,240)
    p = Point(600,240) 

    print p
    print c

    radius = calculate_radius_from_center(p,c)
    assert (radius == 280)
    print radius
