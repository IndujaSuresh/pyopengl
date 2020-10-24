from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def init():
   glClearColor(0.0,0.0,0.0,1.0)
   glColor3f(0.0,0.0,1.0)
   glPointSize(2.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(-100,100,-100,100)

def mid(x1,x2,y1,y2):
  dx = x2-x1
  dy = y2-y1
  
  d = dy - (dx/2);
  x = x1
  y = y1
  
 
  
  while (x < x2):
    x = x+1
    
    if(d<0):
      d = d+dy
    else:
      d = d+(dy-dx)
      y=y+1
    
    plot(x,y)

def plot(x,y):
  glBegin(GL_POINTS)
  glVertex2f(x,y)
  glEnd()
  glFlush()

def Display():
  glClear(GL_COLOR_BUFFER_BIT)
  x1=int(input('x1 coordinate: '))
  y1=int(input ('y1 coordinate: '))
  x2=int(input('x2 coordinate: '))
  y2=int(input('y2 coordinate: '))
  mid(x1,x2,y1,y2)
    
def main():
   glutInit()
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(200,200)
   glutCreateWindow("mid")
   glutDisplayFunc(Display)
   init()

   glutMainLoop()
 
main()
