from text_extraction import TextExtraction
from format_text import TextFormatter
from grid_processor import GridProcessor
import os


class HeatmapProcessor:

  def __init__(self, input_dir, image):
    self.input_dir = input_dir
    self.image = image

  def process(self):
    image_path = os.path.join(self.input_dir, self.image)

    try:
      values = TextExtraction(image_path, self.image)
      clean_values = TextFormatter(values)
      matrix_values = GridProcessor(clean_values, image_path, self.image).create_grid_matrix()

      x_values = list(map(lambda items: items[0], matrix_values))
      y_values = list(map(lambda items: items[1], matrix_values))
      legend_values = list(map(lambda items: items[2], matrix_values))

      return len(x_values), len(y_values), len(legend_values)

    except Exception as e:
      print(f"Error processing image {self.image}: {e}")

  def find_max_length(self, x_max_len, y_max_len, legend_max_len):

    x_len, y_len, legend_len = self.process()

    if x_len > x_max_len:
      x_max_len = x_len
    
    if y_len > y_max_len:
      y_max_len = y_len
    
    if legend_len > legend_max_len:
      legend_max_len = legend_len

    print(x_max_len, y_max_len, legend_max_len)
    return x_max_len, y_max_len, legend_max_len

