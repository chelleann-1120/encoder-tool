import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from region_detection import RegionDetection

class ColorExtractor(RegionDetection):
  '''
  Extracts color in the given image contour
  '''

  def __init__(self, image_path, image_name):
    super().__init__(image_path, image_name)
    self.image_path = image_path
    self.color_legend = self.detect_color_legend()

  def extract_legend_color(self):
    image = Image.open(self.image_path).convert('RGB')
    image_array = np.array(image)

    x, y, width, height = cv2.boundingRect(self.color_legend)
    legend_roi = image_array[y:y+height, x:x+width]
    flattened_colors = [color for row in legend_roi for color in row if not np.array_equal(color, [0, 0, 0])]

    unique_colors = []
    seen = set()
    for color in flattened_colors:
        color_tuple = tuple(color)
        if color_tuple not in seen:
            seen.add(color_tuple)
            unique_colors.append(color)

    unique_colors = np.array(unique_colors)

    plt.figure(figsize=(10, 2))
    plt.imshow([unique_colors], aspect='auto')
    plt.title(self.image_path)
    plt.axis('off')
    plt.show()