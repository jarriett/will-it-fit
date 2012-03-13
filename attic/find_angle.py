from math import sqrt,asin,pi
import Image
#from geometry import *
#
# Assumptions: two tuples([x-intersection,y-intersection])
# returns angle between line and y-axis
#
def angle_from_points(points): 
    a = points[0][0] + points[1][0]
    b  = points[0][1] + points[1][1]
    hyp = sqrt((a*a) + (b*b))
    opp = points[1][0]
    return asin(opp/hyp) * 180/pi

def calc_slope(points):
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]    
    slope = (y2 - y1) / (x2 - x1)
    return slope


def rotate_image(angle):
    img_path = "bitter.jpg"
    img = Image.open(img_path)
    img2 = img.rotate(angle)
    img2.show()
    img2.save("bitter-rotated.jpg")

point1 = (0,5)
point2 = (5,0)
point3 = (0,0)

print point1
print point2
print point3


points = [point1,point2]
angle = angle_from_points(points)
print angle

#rotate_image(angle)

slope = calc_slope(points)
print slope

print calculateIntersectPoint(points)
