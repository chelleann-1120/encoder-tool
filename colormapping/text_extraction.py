import cv2
from PIL import Image
import matplotlib.pyplot as plt
from region_detection import RegionDetection
import pytesseract
import os

class TextExtraction(RegionDetection):
  '''
  Extracts the text in the given region of interest.
  '''
  def __init__(self, image_path, image_name):
    super().__init__(image_path, image_name)
    self.image_path = image_path
    self.img = cv2.imread(image_path)
    self.title_roi = self.detect_title_roi()
    self.yaxis_roi = self.detect_yaxis_roi()
    self.xaxis_roi = self.detect_xaxis_roi()
    self.legend_roi = self.detect_legend_roi()

    if self.image is None:
      raise FileNotFoundError(f"Image not found or unable to read: {image_path}")

  def preprocess_image(self):
    # Example preprocessing steps
    gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    return binary

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
    preprocessed_image = self.preprocess_image()

    x, y, w, h = cv2.boundingRect(largest_contour)
    roi = preprocessed_image[y:y+h, x+w:]

    # Draw bounding box on the original image
    cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert the ROI to a PIL image
    roi_image = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

    # Extract text using Tesseract
    custom_config = r'--psm 6 -c preserve_interword_spaces=1 --oem 3'
    legend_text = pytesseract.image_to_string(roi_image, config=custom_config)
    print("Extracted legend text: \n", legend_text)

    output_path = os.path.join("D:\\encoder-tool\\test-output-images", self.image_name)
    cv2.imwrite(output_path, self.image)  # Save the image with the bounding box

    return legend_text


  def display_image(self):
    plt.imshow(cv2.cvtColor(self.image_np, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide the axis
    plt.show()
