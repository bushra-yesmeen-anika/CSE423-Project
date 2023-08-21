from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#id = input('ENTER ID: ')


def draw_points(x, y):
    glPointSize(3)     # pixel size->by default 1 fix
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(x, y)  # PIXEL DEMONSTARTION CORDINATES
    glEnd()

#FINDING THE GIVEN CORDINATES ZONE
def Find_zone(x_1, y_1, x_2, y_2):
    dx=x_2-x_1
    dy=y_2-y_1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx >= 0 and dy <= 0:
            zone = 7
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx >= 0 and dy <= 0:
            zone = 6
    return zone


def convert_to_zone0(x, y, zone):
    if zone == 0: return x, y
    if zone == 1: return y, x
    if zone == 2: return y, -x
    if zone == 3: return -x, y
    if zone == 4: return -x, -y
    if zone == 5: return -y, -x
    if zone == 6: return -y, x
    if zone == 7: return x, -y


def convertoOrigin(x, y, zone):
    if zone == 0: return x, y
    if zone == 1: return y, x
    if zone == 2: return -y, x
    if zone == 3: return -x, y
    if zone == 4: return -x, -y
    if zone == 5: return -y, -x
    if zone == 6: return y, -x
    if zone == 7: return x, -y

#MID POINT ALGO
def midpoint_line(x1, y1, x2, y2, zone):
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    d_E=2*dy
    d_NE=2*dy-dx
    x=x1
    y=y1
    while (x<x2):
        x_p,y_p=convertoOrigin(x,y,zone)
        draw_points(x_p,y_p)
        if d<0:
            x+=1
            d+=d_E
        else:
            x+=1
            y+=1
            d+=d_NE

#LINE DRAWING
def line_drawing(x1, y1, x2, y2):  #START POINT & END POINT

    curr_z=Find_zone(x1, y1, x2, y2) #DETERMINING CURRENT ZONE
    x1_prime, y1_prime = convert_to_zone0(x1, y1, curr_z)  #CONVERTING TO ZONE 0 ORDER
    x2_prime, y2_prime = convert_to_zone0(x2, y2, curr_z)

    midpoint_line(x1_prime, y1_prime, x2_prime, y2_prime, curr_z) #NEW LINE IN ZONE 0




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # drawing bow
    line_drawing(100, 100, 100, 200)
    #line_drawing(100, 200, 80, 180)
    #line_drawing(100, 200, 120, 180)
    #line_drawing(80, 180, 120, 180)

    #line_drawing(100, 100, 80, 80)
    #line_drawing(100, 100, 120, 80)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL project")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()


