import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pytesseract
from region_detection import ROI
import os

class ColorExtractor(ROI):
  '''
  Extracts color in the given image contour
  '''

  def __init__(self, image_path):
    super().__init__(image_path)
    self.image_path = image_path
    self.color_legend = self.detect_color_legend()