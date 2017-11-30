"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jonathan Kinnard.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    point1 = rg.Point(200,200)
    point2 = rg.Point(300,300)
    circle1 = rg.Circle(point1,50)
    circle1.fill_color = 'green'
    circle2 = rg.Circle(point2,200)
    window1 = rg.RoseWindow(1100, 600)
    circle1.attach_to(window1)
    circle2.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    point1 = rg.Point(200,200)
    circle1 = rg.Circle(point1,50)
    circle1.fill_color = 'blue'
    rect1 = rg.Rectangle(rg.Point(100, 50), rg.Point(300, 200))
    window1 = rg.RoseWindow(1100, 600)
    circle1.attach_to(window1)
    rect1.attach_to(window1)
    window1.render()
    print('now for the circle_and_rectangle() code:')
    print('thickness:',circle1.outline_thickness)
    print('fill color:', circle1.fill_color)
    print('center:', circle1.center)
    print('center x:', circle1.center.x)
    print('center y:', circle1.center.y)

    print('Rect thickness:', rect1.outline_thickness)
    print('Rect fill color:', rect1.fill_color)
    print('Rect Left Top Corner:', rect1.corner_1)
    print('Rect LTC x:', rect1.corner_1.x)
    print('Rect LTC y:', rect1.corner_1.y)
    window1.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # ------------------------------------------------------------------
    line1 = rg.Line(rg.Point(100, 50), rg.Point(200, 30))
    line2 = rg.Line(rg.Point(120, 25), rg.Point(200, 15))
    line2.thickness = 5
    print('now for the lines() code:')
    print('midpoint: ', line2.get_midpoint())
    print('midpoint x: ', line2.get_midpoint().x)
    print('midpoint y: ', line2.get_midpoint().y)
    window1 = rg.RoseWindow(1100, 600)
    line1.attach_to(window1)
    line2.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
