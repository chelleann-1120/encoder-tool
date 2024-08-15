from encoder_tool import *
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

class HeatmapEncoder:

  def __init__(self, input_dir):
    self.input_dir = input_dir

  def find_contours(self, image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours
  
  def run_main(self):

    for image in os.listdir(self.input_dir):
      image_path = os.path.join(self.input_dir, image)
      img = cv2.imread(image_path)
      contours = self.find_contours(img)

      grid = ROI(contours, image_path)
      grid.draw_bounding_boxes()

if __name__ == "__main__":
  input_dir = "D:\\encoder-tool\\generated-heatmaps"
  HeatmapEncoder(input_dir).run_main()