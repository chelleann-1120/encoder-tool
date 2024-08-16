import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from region_detection import ROI
import pytesseract

class TextExtraction(ROI):
  '''
  Extracts the text in the given region of interest.
  '''
  def __init__(self, image_path):
    super().__init__(image_path)
    self.image_path = image_path
    self.img = cv2.imread(image_path)
    #self.legend_color = self.extract_legend_color()
    self.title_roi = self.detect_title_roi()
    self.yaxis_roi = self.detect_yaxis_roi()
    self.xaxis_roi = self.detect_xaxis_roi()
    self.legend_roi = self.detect_legend_roi()

  def extract_title(self):
    title_text = pytesseract.image_to_string(self.title_roi)
    print("Extracted title text:", title_text)
    return title_text

  def extract_yaxis_labels(self):
    yaxis_text = pytesseract.image_to_string(self.yaxis_roi)
    print("Extracted y-axis labels text:", yaxis_text)
    return yaxis_text

  def extract_xaxis_labels(self):
    
    xaxis_roi = self.detect_xaxis_roi()
    
    cropped_image = Image.fromarray(cv2.cvtColor(xaxis_roi, cv2.COLOR_BGR2RGB))
    rotated_image = cropped_image.rotate(-90, expand=True)
    
    xaxis_text = pytesseract.image_to_string(rotated_image)
    print("Extracted x-axis labels text:", xaxis_text)
    return xaxis_text

  def remove_legend(self):

    contour = self.detect_color_legend()
    if contour is not None:
        cv2.drawContours(self.image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    else:
        print("No legend contour found")


  def extract_legend_values(self):
    self.remove_legend()

    largest_contour = self.detect_grid()
    if largest_contour is None:
        return None

    x, y, w, h = cv2.boundingRect(largest_contour)
    roi = self.image_np[y:y+h, x+w:]

    # Convert the ROI to a PIL image
    roi_image = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

    # Extract text using Tesseract
    legend_text = pytesseract.image_to_string(roi_image)
    print("Extracted legend text:", legend_text)
    return legend_text


  def display_image(self):
    plt.imshow(cv2.cvtColor(self.image_np, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide the axis
    plt.show()
