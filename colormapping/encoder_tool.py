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
    self.image_path = image_path
    self.largest_contour = self.detect_grid()
    self.roi_yaxis = self.detect_y_axis()
    self.roi_xaxis = self.detect_x_axis()
    self.roi_legend = self.detect_legend()


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
    # Load the image
    image = Image.open(self.image_path)
    image_np = np.array(image)

    # Draw bounding box around the largest contour
    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Crop the image to the region of interest defined by left_x
    roi_image_np = image_np[y:y + h, roi:x]

    # Display the cropped region of interest
    plt.imshow(roi_image_np)
    plt.axis('off')
    plt.show()
  
  
  def detect_y_axis(self):
    image = Image.open(self.image_path)

    # Draw bounding box around the largest contour
    if self.largest_contour is not None:
      x, y, w, h = cv2.boundingRect(self.largest_contour)
      cv2.rectangle(np.array(image), (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Draw bounding box to the left of the largest contour
    left_x = max(0, x - w)
    self.draw_bounding_boxes(left_x)

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
  
