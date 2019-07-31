# This project automatically plays all modes of the web version of Piano Tiles (http://tanksw.com/piano-tiles/)
## Step 1: Install required libraries (Type in terminals)
  OpenCV: pip install opencv-python
  pynput: pip install pynput
  PIL: pip install PIL
  numpy: pip install numpy
 ## Step 2: Change parameters and calibrate coordinates
  In order to Screem-capture a rectangle space of the screen, we need 2 points. The first point needs to be on the upper left corner of the shape, and the second point needs to be on the bottom right. **Change the first two elements of the "game_cord" variable to the x and y coordinates of the first point, and for 3rd and 4th elements change them to the x and y of the second point.**
  
