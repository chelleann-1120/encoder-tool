import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

class ROI:
  '''
  Identifies the corresponding region of interest. 
  '''

  def __init__(self, image):
    self.image = image

  def detect_gridcells(self):
    print(self.image)
  
  def detect_y_axis(self):
    pass

  def detect_x_axis(self):
    pass

  def detect_legend(self):
    pass

class TextExtraction:
  '''
  Extracting the text within the region of interest
  '''

  def __init__(self):
    pass

  def extract_title(self):
    pass

  def extract_yaxis_labels(self):
    pass

  def extract_xaxis_labels(self):
    pass

  def extract_legend_values(self):
    pass

class TextRemover:
  '''
  Removes the extracted text within the region of interest to avoid overlapping of other
  irrelevant text within the ROI.
  '''

  def __init__(self):
    pass

  def remove_title(self):
    pass

  def remove_xaxis_label(self):
    pass

  def remove_yaxis_label(self):
    pass

  def remove_legend_values(self):
    pass

class ColorExtractor:
  pass
  
