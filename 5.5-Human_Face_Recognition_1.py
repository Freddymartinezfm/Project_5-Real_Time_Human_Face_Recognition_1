#	!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5.5-Human_Face_Recognition.py
#  
#  Copyright 2021 root <root@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



# Real Time Human Face Recognition
# Capturing images from webcam and storing in himan _faces folder 

# Import Computer Vision package - cv2 
import cv2 

# Import Numerical Python package - numpy AS NP
import numpy as np


# Import Time Python Package - time which contains sleep() function
import time

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Check if human face cascade file is loaded
if face_detect.empty():
	raise IOError('Unable to haarcascade_frontalface_default.xml file')
# Defining face_detector function
def face_detector(image):
	# Function detectsfaces and returns the cropped face
	# If not face detected. it returns
	# 
	# 
	# 	
	# Check if user has pressed the esc key
	# c = cv2.waitKey(1)
	# if (c == 27):
	# 	break
	
# Close the capuring device	
# capture.release()

# Destroy all windows 
# cv2.destroyAllWindows()
	pass

print('human face recognition')
