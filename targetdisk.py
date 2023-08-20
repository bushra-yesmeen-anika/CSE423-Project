from OpenGL.GL import *
from OpenGL.GLUT import *


def drawPoints(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midPointCircle(X, Y, r):
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        x += 1
        if d < 0:
            d += 2 * x + 3
        else:
            y -= 1
            d += 2 * (x - y) + 5
        drawPoints(X + x, Y + y)
        drawPoints(X - x, Y + y)
        drawPoints(X + x, Y - y)
        drawPoints(X - x, Y - y)
        drawPoints(X + y, Y + x)
        drawPoints(X - y, Y + x)
        drawPoints(X + y, Y - x)
        drawPoints(X - y, Y - x)


def drawCircles(X, Y, R):
    midPointCircle(X, Y, R) # the big one
    for i in range(50):
        midPointCircle(X, Y, R - i)
    glColor3f(0.0, 0.0, 0.0)
    midPointCircle(X, Y, R - 50)
    glColor3f(0.0, 0.0, 1.0)
    midPointCircle(X, Y, R - 100)
    for i in range(100, 150):
        midPointCircle(X, Y, R - i)
    glColor3f(1.0, 0.0, 0.0)
    midPointCircle(X, Y, R - 150)
    for i in range(150, 200):
        midPointCircle(X, Y, R - i)
    glColor3f(1.0, 1.0, 0.0)
    midPointCircle(X, Y, R - 200)
    for i in range(200, 250):
        midPointCircle(X, Y, R - i)


def iterate():
    glViewport(0, 0, 900, 900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 900, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    drawCircles(350, 350, 250)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(900, 900)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"CSE423 Lab Assignment03")
glutDisplayFunc(showScreen)

glutMainLoop()