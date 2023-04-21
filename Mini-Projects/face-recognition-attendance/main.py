import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

#Load Known faces
shashank_image= face_recognition.load_image_file("faces/shashank.jpg")