import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


class ROI:
  '''
  Identifies the corresponding region of interest. 
  '''

  def __init__(self, contours, image_path):
    self.contours = contours
    self.image = Image.open(image_path)
    self.image_np = np.array(self.image)
    self.largest_contour = self.detect_grid()

  def detect_grid(self):
    max_area = 0
    largest_contour = None

    for contour in self.contours:
      area = cv2.contourArea(contour)
      if area > max_area:
        max_area = area
        largest_contour = contour

    return largest_contour

  def draw_bounding_boxes(self, roi):

    # Display the cropped region of interest
    plt.imshow(roi)
    plt.axis('off')
    plt.show()
  
  def detect_title(self):
    
    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      top = max(0, y - h)
      roi_above = self.image_np[top:y, :]
      self.draw_bounding_boxes(roi_above)
  
  def detect_y_axis(self):

    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      left = max(0, x - w)
      roi_yaxis = self.image_np[y:y + h, left:x]
      self.draw_bounding_boxes(roi_yaxis)

  def detect_x_axis(self):

    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      bottom = min(self.image_np.shape[0], y + 2 * h)
      roi_xaxis = self.image_np[y + h:bottom, x:x + w]
      self.draw_bounding_boxes(roi_xaxis)

  def detect_legend(self):

    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      right = min(self.image_np.shape[1], x + 2 * w)
      roi_legend = self.image_np[y:y + h, x + w:right]
      self.draw_bounding_boxes(roi_legend)

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


class ColorExtractor:
  pass
  
