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
# Capturing images from webcam and storing in himan _faces folder (must run as sudo)

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
	# Function detects faces and returns the cropped face
	# If not face detected. it returns the input image 
	# Convert RGB to gray using cv2.COLOR_BGR2GRAY built-in function
	# BGR (bytes are reversed)
	# cv2.CvtColor: Converts image from one color space to another 
	#
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect objects(faces) of different sizes using cv2.CascadeClassifer.detectMultiScale
	# cv2.CascadeClassifier.detectMultiScale(gray, scaleFactor, minNeighbors)

	# scaleFactor: Specifies the image size to be reduced
	# Faces closer to the camera appear bigger than those faces in the back


	# minNeighbors:  Specifies the number of neighbors each rectangle should have to retain it
	# Higher value results in less detections but with higher quality

	face_detection = face_detect.detectMultiScale(gray, 1.3, 5)

	if (face_detection is ()):
		return None

	# Faces are cropped when they detected
	for (x, y, w, h) in face_detection:
		face_cropped = image[y:y+h, x:x+w]
	return face_cropped

























# Initialzing video capturing object
capture = cv2.VideoCapture(0)
# One camera will be connected by passing 0 or -1
# Second camera can be selected by passing 2

# Initialize face_count to zero
face_count = 0

# Initialize while loop and execute until esc key is pressed or face_count == 20
while True:
	# Start capturing frames
	
	
	ret, capturing = capture.read()

	if face_detector(capturing) is not None:
		face_count += 1
		# Resize the frame using cv2.resize built-in function
		# cv2.resize(capturing, output image size, x scale, y scale, interpolation)
		resized_frame = cv2.resize(face_detector(capturing), (250,250))

		# Convert RGB to gray using cv2.COLOR_BGR2GRAY built-in function
		# BGR (bytes are reversed)
		# cv2.CvtColor: Converts image from one color space to another 
		gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

		# Cropped faces are saved in human_faces folder
		# Unique name is given to each cropped face
		path = '/var/image-processing/self-course-codes/Project_5-Real_Time_Human_Face_Recognition/human_faces/' + str(face_count) + '.jpg'

		# Save cropped faces in specified path using imwrite built-in function
		cv2.imwrite(path, gray)
		print('human face saved to ' + path)

		# TODO 
		cv2.putText(gray, str(face_count), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)


		# TODO
		cv2.imshow('Cropped', gray)
	else:
		print('face not detected')
		pass
 	
	# Check if user has pressed the esc key 
	if (cv2.waitKey(1) == 27 or face_count == 20):
		break
	
# Close the capuring device	
capture.release()

# Destroy all windows 
cv2.destroyAllWindows()
print('human face recognition')
