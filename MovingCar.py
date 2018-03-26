from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *
def rectangle(x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b, typ):
    glColor(r, g, b)
    glBegin(typ)
    glVertex3d(x, y, z)
    glVertex3d(x1, y1, z1)
    glVertex3d(x2, y2, z2)
    glVertex3d(x3, y3, z3)
    glEnd()
def circle(rs, s, e, xnaught, ynaught, r, g, b, typ):
    glColor(r, g, b)
    glBegin(typ)
    for theta in arange(s, e, 0.01):
        x = rs * cos(theta) + xnaught
        y = rs * sin(theta) + ynaught
        glVertex2d(x, y)
    glEnd()
def triangle(x1, y1, x2, y2, x3, y3, r, g, b, typ):
    glColor(r, g, b)
    glBegin(typ)
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()
def line(x, y, x1, y1, r, g, b, typ):
    glColor(r, g, b)
    glBegin(typ)
    glVertex2d(x,y)
    glVertex2d(x1, y1)
    glEnd()
def myInit():
      glMatrixMode(GL_PROJECTION)
      glClearColor(1, 1, 1, 1)
      glClear(GL_COLOR_BUFFER_BIT)
      glOrtho(-10, 10,-10, 10, -10, 10)
      gluPerspective(6, 1, 0.1, 50)
      gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)
x = 0
angle = 0
k = 0.1
y = 0.001
def draw():
    global x
    global angle
    global y
    global k
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0.5, 0.5, 0.5)
    glTranslate(0, 0, -8)
    glScale(35, 0.25, 1)
    glutSolidCube(5)
    glLoadIdentity()
    rectangle(-x, -3, -1, -x + 5, -3, -1, -x + 5, -3, -1.5, -x, -3, -1.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    rectangle(-x, -3, -2, -x + 5, -3, -2, -x + 5, -3, -2.5, -x, -3, -2.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    rectangle(-x + 10, -3, -1, -x + 15, -3, -1, -x + 15, -3, -1.5, -x + 10, -3, -1.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    rectangle(-x + 10, -3, -2, -x + 15, -3, -2, -x + 15, -3, -2.5, -x + 10, -3, -2.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    rectangle(-x - 15, -3, -1, -x - 10, -3, -1, -x - 10, -3, -1.5, -x - 15, -3, -1.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    rectangle(-x - 15, -3, -2, -x - 10, -3, -2, -x - 10, -3, -2.5, -x - 15, -3, -2.5, 1, 1, 1, GL_POLYGON)
    glLoadIdentity()
    glColor3f(0.5, 0.5, 0.5)
    glTranslate(0, 0, 8)
    glScale(30, 0.25, 2)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(x, 0.25 * 5, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, 0.5 * 2.5)
    glRotatef(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 12, 8)
    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, -0.5 * 2.5)
    glRotatef(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 12, 8)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, 0.5 * 2.5)
    glRotatef(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 12, 8)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, -0.5 * 2.5)
    glRotatef(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 12, 8)
    glColor3f(0.6, 0.3, 0)
    glLoadIdentity()
    glTranslate(-x, 2.5, -8)
    glScale(0.08, 1, 0.08)
    glutSolidCube(5)
    glColor3f(0, 0.6, 0)
    glLoadIdentity()
    glTranslate(-x, 4, -8)
    glScale(1, 1, 1)
    glutSolidSphere(2, 90, 120)
    glColor3f(0.6, 0.3, 0)
    glLoadIdentity()
    glTranslate(-x - 5, 2.5, -8)
    glScale(0.08, 1, 0.08)
    glutSolidCube(5)
    glColor3f(0, 0.6, 0)
    glLoadIdentity()
    glTranslate(-x - 5, 4, -8)
    glScale(1, 1, 1)
    glutSolidSphere(2, 90, 120)
    if x > 10:
        y = -0.001
        k = -0.1
    elif x < -1.9:
        y = 0.001
        k = 0.1
    x += y
    angle -= k
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"Sec6")
glutInitWindowSize(100, 100)
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()
