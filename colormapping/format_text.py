import cv2
import numpy as np

class TextFormatter:
    
  def __init__(self, text):
    self.text = text

  def format_title(self):
    title = self.text.extract_title()
    title = title.replace('\n', ' ')
    return title
  
  def clean_yaxis_label(self):
    
    yaxis_labels = self.text.extract_yaxis_labels()
    array_yaxis = yaxis_labels.splitlines()
    array_yaxis = [label for label in array_yaxis if label]
    
    return array_yaxis

  def clean_xaxis_label(self):

    xaxis_labels = self.text.extract_xaxis_labels()
    array_xaxis = xaxis_labels.splitlines()
    array_xaxis = [label for label in array_xaxis if label]
    
    return array_xaxis

  def clean_legend_values(self):

    legend_values = self.text.extract_legend_values()
    array_legend_values = legend_values.splitlines()
    array_legend_values = [value for value in array_legend_values if value]

    return array_legend_values


class CellLabelMapping:

  def __init__(self, text):
    super().__init__(text)

  def map_cell_labels(self):
    pass


class GridProcessor(TextFormatter):

  def __init__(self, text):
    super().__init__(text)
    self.title = self.format_title()
    self.yaxis_labels = self.clean_yaxis_label()
    self.xaxis_labels = self.clean_xaxis_label()
    self.legend_values = self.clean_legend_values()
    self.yaxis_len = len(self.yaxis_labels)
    self.xaxis_len = len(self.xaxis_labels)
    self.colors = self.text.extract_legend_color()

  def grid_color_matrix(self):

    cell_matrix = [[self.xaxis_labels[i] for i in range(self.xaxis_len)] for _ in range(self.yaxis_len)]

    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(self.text.largest_contour)

    # Crop the region of interest from the original image using the bounding box
    cropped_image = self.text.image[y:y+h, x:x+w]

    num_regions_y = self.yaxis_len
    num_regions_x = self.xaxis_len

    # Calculate the new dimensions that are divisible by the specified number of regions
    new_height = (h // num_regions_y) * num_regions_y
    new_width = (w // num_regions_x) * num_regions_x

    # Resize the cropped image to the new dimensions while maintaining the aspect ratio
    resized_image = cv2.resize(cropped_image, (new_width, new_height))
    resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Calculate the width and height of each smaller region
    region_height = new_height // num_regions_y
    region_width = new_width // num_regions_x

    hex_values = []
    dominant_colors = []

    # Extract and display each smaller region
    for i in range(num_regions_y):
      for j in range(num_regions_x):
          
        start_y = i * region_height
        end_y = start_y + region_height
        start_x = j * region_width
        end_x = start_x + region_width
        smaller_region = resized_image_rgb[start_y:end_y, start_x:end_x]

        # Convert the smaller region to a 2D array of pixels
        pixels = smaller_region.reshape((-1, 3))
        pixels = np.float32(pixels)

        # Define criteria and apply K-means clustering
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        k = 1
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Get the dominant color
        dominant_color = centers[0].astype(int)
        dominant_colors.append(dominant_color)

        # Convert the dominant color to hex
        hex_color = "#{:02x}{:02x}{:02x}".format(dominant_color[0], dominant_color[1], dominant_color[2])
        hex_values.append(hex_color)

    print(self.text.image_path, len(hex_values))

  # Key value pair, title: Size,, #hexvalue: 2.1+e10 to 2.3+e11, etc.,
  def create_legend_matrix(self):
    
    title = self.legend_values[0]
    legend_dict = {"title": title}
    legend_dict.update({self.colors[i]: self.legend_values[i + 1] for i in range(len(self.colors))})
    
    return legend_dict
