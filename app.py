from wif_lib.geometry import  *
import pygame

pt1 = Point(600,240)
pt2 = Point(40,240)
pt3 = Point(320,120)
pt4 = Point(420,120)

pts = [pt1,pt2,pt3,pt4]

lines = create_enclosed_shape_from_points(pts)

screen = pygame.display.set_mode((640, 480))
running = 1 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 0, 0))
        
    p1 = Point(600,240)
    p2 = Point(40,240)
    
    
    #Draw a horizontal line
    for line in lines:
        pygame.draw.line(screen,
            (0, 0, 255),
            (line.start.x, line.start.y),
            (line.finish.x, line.finish.y))
    
    #draw to screen
    pygame.display.flip()
