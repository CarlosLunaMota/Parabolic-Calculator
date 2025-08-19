from pyx  import *
from math import *

BLACK  = color.rgbfromhexstring("#000")
DARK   = color.rgbfromhexstring("#666")
GREY   = color.rgbfromhexstring("#BBB")
LIGHT  = color.rgbfromhexstring("#DDD")
WHITE  = color.rgbfromhexstring("#FFF")

YELLOW  = color.rgbfromhexstring("#FF6")
ORANGE  = color.rgbfromhexstring("#FC6")
RED     = color.rgbfromhexstring("#F66")
MAGENTA = color.rgbfromhexstring("#F6F")
VIOLET  = color.rgbfromhexstring("#C6F")
BLUE    = color.rgbfromhexstring("#66F")
CYAN    = color.rgbfromhexstring("#6FF")
GREEN   = color.rgbfromhexstring("#6F6")
BROWN   = color.rgbfromhexstring("#B68E78")

# PYX STYLES:
LINE   = [style.linecap.round, style.linejoin.round, style.linewidth.normal]
THIN   = [style.linewidth.THIN]
THICK  = [style.linewidth.thick]
DASHED = [style.linestyle.dashed]
DOTTED = [style.linestyle.dotted]

text.set(text.LatexEngine)
text.preamble(r"\usepackage{lmodern}")
text.preamble(r"\renewcommand{\familydefault}{\sfdefault}")
text.preamble(r"\usepackage[cm]{sfmath}")

def FILLED(color): return [color, deco.filled([color])]

def draw_calculator(filename, LOGO=None, H=21, W=29.7, M=2, ticks=0.09):

  X = W - 2*M
  Y = H - 2*M;

  print(X/2, Y/10);
 
  CANVAS = canvas.canvas()

  # Background:
  CANVAS.stroke(path.path(path.moveto(0.05-W/2,   0.05-M),
                          path.lineto(W/2-0.05,   0.05-M),
                          path.lineto(W/2-0.05, H-M-0.05),
                          path.lineto(0.05-W/2, H-M-0.05),
                          path.closepath()), LINE+THIN+[WHITE])

  # Y axis
  CANVAS.stroke(path.path(path.moveto(0, 0),
                          path.lineto(0, Y)), LINE)

  for y in range(1,101):
    CANVAS.stroke(path.path(path.moveto(-ticks/2, y*Y/100),
                            path.lineto( ticks/2, y*Y/100)), LINE)
    
  for y in range(5,101,5):
    CANVAS.stroke(path.path(path.moveto(-ticks, y*Y/100),
                            path.lineto( ticks, y*Y/100)), LINE)

    CANVAS.text(2*ticks, y*Y/100, str(y), [text.halign.left, text.valign.middle])

  # Parabola
  for x in range(1,101):
    CANVAS.stroke(path.path(path.moveto((x-1)*X/200, (x-1)*(x-1)*Y/10000),
                            path.lineto(x*X/200, x*x*Y/10000)), LINE)
    CANVAS.stroke(path.path(path.moveto(-(x-1)*X/200, (x-1)*(x-1)*Y/10000),
                            path.lineto(-x*X/200, x*x*Y/10000)), LINE)

  for x in range(-100,101):

    V = (2*x*Y/1000,-X/20)
    K = ticks/2/sqrt(V[0]*V[0] + V[1]*V[1])

    CANVAS.stroke(path.path(path.moveto(x*X/200 + V[0]*K, x*x*Y/10000 + V[1]*K),
                            path.lineto(x*X/200 - V[0]*K, x*x*Y/10000 - V[1]*K)), LINE)
    
  for x in range(-100,101,5):

    V = (2*x*Y/1000,-X/20)
    K = ticks/sqrt(V[0]*V[0] + V[1]*V[1])

    CANVAS.stroke(path.path(path.moveto(x*X/200 + V[0]*K, x*x*Y/10000 + V[1]*K),
                            path.lineto(x*X/200 - V[0]*K, x*x*Y/10000 - V[1]*K)), LINE)
  
  for x in range(-10,11):

    V = (2*x*Y/100,-X/20)
    K = ticks*3.5/sqrt(V[0]*V[0] + V[1]*V[1])

    CANVAS.text(x*X/20 + V[0]*K, x*x*Y/100 + V[1]*K, str(abs(x)),
               [text.halign.center, text.valign.middle])
  
  # Logo
  if LOGO: CANVAS.insert(bitmap.bitmap(X/2-3.5, 0.3,
                         bitmap.jpegimage(LOGO), compressmode=None))
  
  CANVAS.writeSVGfile(filename)
  CANVAS.writePDFfile(filename)

def draw(filename, LOGO=None, T=[], EXAMPLE=False, H=21, W=29.7, M=2, tick=0.09):

  X = W - 2*M
  Y = H - 2*M;
 
  CANVAS = canvas.canvas()

  # Background (for paper size):
  CANVAS.stroke(path.path(path.moveto(0.05-W/2,   0.05-M),
                          path.lineto(W/2-0.05,   0.05-M),
                          path.lineto(W/2-0.05, H-M-0.05),
                          path.lineto(0.05-W/2, H-M-0.05),
                          path.closepath()), LINE+THIN+[WHITE])

  # Example:
  if EXAMPLE:
    CANVAS.stroke(path.path(path.moveto(-6*X/20, 36*Y/100),
                            path.lineto( 7*X/20,  49*Y/100)),
                            LINE+[MAGENTA])
  
  # X axis
  for x in range(-100,101,10):
    CANVAS.stroke(path.path(path.moveto(x*X/200, x*x*Y/10000),
                            path.lineto(x*X/200, 0)), LINE+[GREY])

  for x in range(-95,101,10):
    CANVAS.stroke(path.path(path.moveto(x*X/200, x*x*Y/10000),
                            path.lineto(x*X/200, 0)), LINE+[GREY]+DASHED)

  CANVAS.stroke(path.path(path.moveto(-X/2, 0),
                          path.lineto( X/2, 0)), LINE)

  for x in range(-100,101):
    CANVAS.stroke(path.path(path.moveto(x*X/200, -tick/2),
                            path.lineto(x*X/200,  0 if abs(x)<5 else tick/2)), LINE)
    
  for x in range(-100,101,5):
    CANVAS.stroke(path.path(path.moveto(x*X/200, -tick),
                            path.lineto(x*X/200,  0 if abs(x)<10 else tick)), LINE)

  for x in range(-10,11):
    CANVAS.text(x*X/20, -2*tick , str(x)+ (r"\;" if x<0 else ""),
                [text.halign.center, text.valign.top])

  # Y axis
  CANVAS.stroke(path.path(path.moveto(0, 0),
                          path.lineto(0, Y)), LINE)

  for y in range(1,101):
    CANVAS.stroke(path.path(path.moveto(-tick/2, y*Y/100),
                            path.lineto( tick/2, y*Y/100)), LINE)
    
  for y in range(5,101,5):
    CANVAS.stroke(path.path(path.moveto(-tick, y*Y/100),
                            path.lineto( tick, y*Y/100)), LINE)

  for y in range(5,101,5):
    CANVAS.text(2*tick, y*Y/100, str(y), [text.halign.left, text.valign.middle])

  # Parabola
  for x in range(1,101):
    CANVAS.stroke(path.path(path.moveto((x-1)*X/200, (x-1)*(x-1)*Y/10000),
                            path.lineto(x*X/200, x*x*Y/10000)), LINE+THICK)
    CANVAS.stroke(path.path(path.moveto(-(x-1)*X/200, (x-1)*(x-1)*Y/10000),
                            path.lineto(-x*X/200, x*x*Y/10000)), LINE+THICK)

  # Logo
  if LOGO: CANVAS.insert(bitmap.bitmap(X/2-3.5, 0.3,
                         bitmap.jpegimage(LOGO), compressmode=None))
  
  # Text
  if T:
    #CANVAS.text(-0.75, Y, T[0], [text.halign.right, text.valign.top])
    for i,t in enumerate(T):
        CANVAS.text(-0.75, Y-1*i, t, [text.halign.right, text.valign.top])
  
  CANVAS.writeSVGfile(filename)
  CANVAS.writePDFfile(filename)

if __name__ == "__main__":

  CAT = [r"\large Uneix dos punts de la par\`{a}bola $y\!=\!x^2$ amb un segment de recta.",
         r"\large Qu\`{e} observes a l'eix vertical? Passar\`{a} sempre? Com ho saps?",
         r"\large Qu\`{e} passa quan els punts s\'{o}n a un mateix costat de l'eix?",
         r"\large Qu\`{e} passa quan els punts s'apropen molt l'un a l'altre?"]

  ENG = [r"\large Join any two points on the parabola $y\!=\!x^2$ with a straight line.",
         r"\large What do you observe on the vertical axis? Can you prove it?",
         r"\large What happens if the two points are on the same side?",
         r"\large What happens when the points get very close?"]

  draw("La Paràbola Multiplicadora", "Logo MMACA.jpg", CAT, True)
  draw("The Multiplying Parabola",   "Logo MMACA.jpg", ENG, True)
  draw("Parabola", "Logo MMACA.jpg")
  draw("Parabola - Blank")
  draw_calculator("Parabolic Calculator", "Logo MMACA.jpg")
  draw_calculator("Parabolic Calculator - Blank")
