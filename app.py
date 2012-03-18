from wif_lib.geometry import  *
from wif_lib.convex_hull import  *
from math import pi
import pygame

def draw_shape(shape,color):
    for line in shape:
        pygame.draw.line(screen,
            color,
            (line.start.x, line.start.y),
            (line.finish.x, line.finish.y))
  
pt1 = Point(100,100)
pt2 = Point(200,200)
pt3 = Point(100,300)
pt4 = Point(300,300)
pt5 = Point(300,100)

pts = [pt1,pt2,pt3,pt4,pt5]

hull_points =  generate_convex_hull(pts) 
hull = strip_non_hull_points(pts,hull_points)

for pt in hull:
  print pt

lines = create_enclosed_shape_from_points(pts)
hull_shape = create_enclosed_shape_from_points(hull)
screen = pygame.display.set_mode((640, 480))
running = 1 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 0, 0))
        
    p1 = Point(600,240)
    p2 = Point(40,240)
    
    draw_shape(lines,(0,0,255)) 
    draw_shape(hull_shape,(0,255,0)) 
    
    #Draw a horizontal line
#    shape = rotate_a_shape(lines,pi/2,get_center_of_canvas(640,480)) 

#    draw_shape(shape)
    #draw to screen
    pygame.display.flip()



